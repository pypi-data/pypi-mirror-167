#!/usr/bin/env python
r"""helpers for the Xymon Python-based library
"""
# stdlib
from __future__ import annotations
from functools import partial
from typing import TypedDict
import re

# local
from . import Xymon, Xymons


class TypeDefaults(TypedDict, total=False):
    hostname: str | None
    testname: str | None


class Color(float):
    """describe a Xymon color (status)"""

    name = None
    """textual representation of the color
    """

    def __new__(cls, x, name: str):
        result = float.__new__(cls, x)
        result.name = name
        return result

    def __str__(self) -> str:
        return self.name or ""

    def __repr__(self) -> str:
        return f"<Color {self.name}>"


class Helper(object):
    r"""make it even easier to use Xymon objects

    Examples::

       # create an object with default hostname and default service
       >>> x = Helper(Xymon('xymon.example.net'), 'www.intra.example.net', 'http')
       # add a message
       >>> x+= '&red something gone pear shaped\n'
       # send the content of the current buffer with text added at the end
       # override the global color of the message (from red to yellow)
       # clear the buffer
       >>> x.status('but it is not *that* bad', color=yellow)
       # now the buffer has been cleared,
       # send another message, with the same hostname but a different service name
       >>> x.status('do not shoot the messenger!', service='logs')
    """
    r_color = re.compile(r"&(green|yellow|red|clear)\b")
    """extract status identifiers
    """

    defaults: TypeDefaults  #: default hostname and testname passed to Xymon

    def __init__(self, xymon: Xymon | Xymons, hostname: str | None = None, testname: str | None = None):
        self.defaults = {}
        if hostname:
            self.defaults["hostname"] = hostname
        if testname:
            self.defaults["testname"] = testname
        self.data: str = ""
        self.xymon = xymon

    def __iadd__(self, other: str):
        self.data += other
        return self

    @property
    def color(self) -> Color:
        """current highest level color or :data:`clear` if none found"""
        return max(self.get_colors(self.data, clear))

    @classmethod
    def get_colors(cls, text: str, default: Color | None = None) -> list[Color]:
        """extract all colors from text

        :param text:
        :param default:
        """
        result = [color_map[f"{color!s}"] for color in cls.r_color.findall(text)]
        if not result and default is not None:
            result += [default]
        return result

    def status(self, message: str = "", **kwargs) -> str:
        """call :meth:`Xymon.status`

        Generate the query from merging :attr:`defaults`
        with any additional `kwargs` given.
        The final message is the addition of `message` to
        any existing :attr:`data` and `kwargs['text']`.
        Status `color` will be guessed from the message text
        if not explicitly set in the `kwargs`.

        :param message:
        :param kwargs: additional parameters
        """
        params: dict = self.defaults.copy()
        params.update(kwargs)
        text = kwargs.get("text", "")
        # build the message
        params["text"] = f"{self.data!s}{message!s}{text!s}"
        # empty the buffer
        self.data = ""

        if "color" not in kwargs:
            # no color has been explicitly set, find it from the text
            colors = self.get_colors(params["text"], clear)
            params["color"] = max(colors)

        return self.xymon.status(**params)

    def __getattr__(self, name: str):
        def _host(name, **kwargs):
            params = {"hostname": self.defaults["hostname"]}
            params.update(kwargs)
            return getattr(self.xymon, name)(**params)

        def _host_test(name, **kwargs):
            params = self.defaults.copy()
            params.update(kwargs)
            return getattr(self.xymon, name)(**params)

        def _host_test_text(name, message="", **kwargs):
            params = self.defaults.copy()
            params.update(kwargs)
            # build the message
            text = kwargs.get("text", "")
            params["text"] = f"{self.data!s}{message!s}{text!s}"
            # empty the buffer
            self.data = ""
            return getattr(self.xymon, name)(**params)

        if name in {"rename", "client", "clientlot", "modify"}:
            return partial(_host, name)

        if name in {"disable", "enable", "query", "drop", "xymondlog", "xymondxlog", "modify"}:
            return partial(_host_test, name)

        if name in {"notify", "data"}:
            return partial(_host_test_text, name)

        return getattr(self.xymon, name)


purple = Color("inf", "purple")
blue = Color("nan", "blue")
clear = Color(0, "clear")
green = Color(1, "green")
yellow = Color(2, "yellow")
red = Color(3, "red")

#: a list of valid "colors"
color_map = {
    purple: purple,
    blue: blue,
    clear: clear,
    green: green,
    yellow: yellow,
    red: red,
    "purple": purple,
    "blue": blue,
    "clear": clear,
    "green": green,
    "yellow": yellow,
    "red": red,
}
