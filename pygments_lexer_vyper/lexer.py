# -*- coding: utf-8 -*-
"""
    pygments.lexers.vyper
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for the Vyper language.

    :copyright: Copyright 2006-2015 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, default, using, \
    this, words, combined
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Other

__all__ = ['VyperLexer']


class VyperLexer(RegexLexer):
    """
    For Vyper source code.
    """

    name = 'Vyper'
    aliases = ['vy', 'v.py', 'vyper']
    filenames = ['*.vy', '*.v.py']
    mimetypes = []

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    def type_names(prefix, sizerange):
        """
        Helper for type name generation, like: bytes1 .. bytes32
        """


    def type_names_mn(prefix, sizerangem, sizerangen):
        """
        Helper for type name generation, like: fixed0x8 .. fixed0x256
        """


    tokens = {} # tokens
