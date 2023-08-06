#!/usr/bin/env python
"""a CLI for the library
"""
# stdlib
from __future__ import annotations
from argparse import Action, Namespace, ArgumentParser, RawDescriptionHelpFormatter, _SubParsersAction
from itertools import zip_longest
from collections import namedtuple
from inspect import getfullargspec
from pprint import pprint

import logging
import os
import json
import sys

# dependencies
try:  # pragma: no cover
    import yaml

    YAML = True
except ImportError:  # pragma: no cover
    YAML = False

# local
from . import __version__, Xymon, Xymons


logger = logging.getLogger("xymon")
REQUIRED = object()


class XymonServer(namedtuple("XymonServer", ("hostname", "port"))):
    """describe a Xymon server"""

    __slots__ = ()

    def __new__(cls, hostname: str, port: int):
        return super(XymonServer, cls).__new__(cls, hostname, int(port or 1984))

    def __str__(self) -> str:
        return f"{self.hostname}:{self.port}"


class ActionServer(Action):
    """separate hostname and port"""

    def __call__(self, parser, namespace, values, option_string=None) -> None:
        server, port = values.partition(":")[::2]
        if getattr(namespace, self.dest) is None:
            setattr(namespace, self.dest, [])
        getattr(namespace, self.dest).append(XymonServer(server, port))


class KWArgs(dict):
    """a dict whose string representation is like arguments for a method

    Example:

    >>> str(KWArgs(foo='bar', x=(4, 2)))
    "foo='bar', x=(4, 2)"
    """

    @classmethod
    def from_namespace(cls, namespace: Namespace, exclude: set | None = None) -> KWArgs:
        """build a KWArgs object from a :class:`Namespace` object

        :param namespace:
        :param exclude: key to be excluded
        """
        __exclude = exclude if exclude else {}
        # pylint: disable=protected-access
        return cls((k, v) for k, v in namespace._get_kwargs() if k not in __exclude)

    def __str__(self) -> str:
        return ", ".join(f"{k}={self[k]!r}" for k in sorted(self))


class OutputFormatter(object):
    """Output arbitrary data to a given format (plain text, JSON or YAML)."""

    __formatter = None

    @classmethod
    def formats(cls) -> list[str]:
        """List available formats"""
        return [k[3:] for k in cls.__dict__ if k[:3] == "to_"]

    def __init__(self, fmt: str, out=sys.stdout):
        self.__fp = out
        try:
            self.__formatter = getattr(self, f"to_{fmt}")
        except AttributeError as exception:
            raise ValueError(f"unsupported format: {fmt}") from exception

    def __call__(self, *args, **kwargs):
        return self.__formatter(*args, **kwargs)

    def to_text(self, data) -> None:
        # :envvar:`COLUMNS` is not exported...
        if os.environ.get("COLUMNS") is None:
            try:
                os.environ["COLUMNS"] = str(os.get_terminal_size().columns)
            except OSError:
                os.environ["COLUMNS"] = "80"
        try:
            width = int(os.environ["COLUMNS"])
        except (KeyError, ValueError):
            logger.warning("unable to get terminal width", exc_info=True)
            width = 80

        pprint(
            data,
            self.__fp,
            width=width,
        )

    def to_json(self, data) -> None:
        json.dump(
            data,
            self.__fp,
            indent=2,
            default=str,
            sort_keys=True,
        )
        self.__fp.write("\n")

    def to_yaml(self, data):
        if not YAML:
            return self.to_json(data)

        def represent_named_tuple(_self: yaml.SafeDumper, _data):
            if hasattr(_data, "_asdict"):
                return _self.represent_dict(_data._asdict())
            return _self.represent_list(_data)

        def represent_default(_self: yaml.SafeDumper, _data):
            return _self.represent_str(str(_data))

        yaml.SafeDumper.add_multi_representer(tuple, represent_named_tuple)
        yaml.SafeDumper.add_representer(None, represent_default)

        yaml.dump(
            data,
            self.__fp,
            yaml.SafeDumper,
            default_flow_style=False,
            explicit_start=True,
            explicit_end=True,
        )


def build_parser_for(parser: _SubParsersAction, obj: type):
    """inspect a class `obj` to generate subparsers based on its public methods

    :param parser:
    :param obj: a class to generate parser for
    """
    # pylint: disable=too-many-nested-blocks
    for k, v in sorted(obj.__dict__.items()):
        if k[0] != "_" and callable(v):
            # use the very first docstring line as short help
            teaser = (v.__doc__ or "").partition("\n")[0]
            sub = parser.add_parser(k, help=teaser)
            # the usage is what is shown for: ACTION -h
            sub.usage = (v.__doc__ or "").rstrip()
            argspec = getfullargspec(v)
            args = zip_longest(
                argspec.args[::-1], () if argspec.defaults is None else argspec.defaults[::-1], fillvalue=REQUIRED
            )

            for arg, default in list(args)[::-1]:
                if arg not in {"self", "cls"}:
                    kwargs = {}
                    if default is REQUIRED:
                        kwargs["required"] = True
                        kwargs["help"] = "required"
                    else:
                        kwargs["default"] = default
                        kwargs["help"] = "default: %(default)r"
                        if default is not None:
                            kwargs["type"] = type(default)
                    sub.add_argument(f"--{arg!s}", **kwargs)


def get_parser() -> tuple[ArgumentParser, set]:
    """get the main options parser

    :return: a parser and a set containing initial parser flags
    """
    parser = ArgumentParser(
        description="A Xymon client",
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument("-q", "--quiet", action="store_const", const=0, dest="verbose", default=1)
    parser.add_argument("-v", "--verbose", action="count")
    parser.add_argument("-n", "--dry-run", dest="noop", action="store_true")
    parser.add_argument("-f", "--format", choices=OutputFormatter.formats(), default="text")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "-s", "--server", action=ActionServer, help="comma separated list of Xymon servers (host:port)", required=True
    )
    parser.add_argument("--sender", help="sender name exposed to Xymon (default: current machine name)")

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="action",
        help="Command passed to Xymon server(s); " "refer to https://www.xymon.com/help/manpages/man1/xymon.1.html",
        metavar="[ACTION [-h] [OPTIONS]]",
    )

    # pylint: disable=protected-access
    parser_flags = {action.dest for action in parser._actions}

    build_parser_for(subparsers, Xymon)

    return parser, parser_flags


def main():  # pragma: no cover
    """execute the CLI"""
    parser, exclude = get_parser()
    arg = parser.parse_args()

    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        datefmt="%F %T",
        level=min(max(logging.CRITICAL - (arg.verbose * 10), logging.DEBUG), logging.CRITICAL),
    )

    if len(arg.server) > 1:
        # FIXME: the port is not per server
        xymon = Xymons([_.hostname for _ in arg.server], arg.server[0].port, arg.sender)
    else:
        xymon = Xymon(arg.server[0].hostname, arg.server[0].port, arg.sender)

    func = getattr(xymon, arg.action)
    kwargs = KWArgs.from_namespace(arg, exclude)

    logger.debug("going to execute: %s(%s))", arg.action, kwargs)
    if arg.noop:
        logger.info("dry-run mode, no further action is performed")
    else:
        result = func(**kwargs)
        OutputFormatter(arg.format)(result)


if __name__ == "__main__":  # pragma: no cover
    main()
