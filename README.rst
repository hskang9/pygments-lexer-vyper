pygments-lexer-vyper
=======================

Vyper lexer for Pygments, distributed as a PyPI package.

This package is created for Vyper's [# TO DO - Create and Implement Vyper Lexer](https://github.com/ethereum/vyper/blob/master/docs/conf.py).
It is extended from [pygments-lexer-solidity](https://gitlab.com/veox/pygments-lexer-solidity).


Installation
------------

``pip install pygments-lexer-vyper``


Usage
-----

Depends on doc-building infrastructure.

Sphinx
^^^^^^

Have this in Sphinx's ``conf.py``:

.. code-block:: python
   
   from sphinx.highlighting import lexers
   from pygments_lexer_vyper import VyperLexer
   lexers['vyper'] = VyperLexer()

Then use ``.. code-block:: vyper`` Vyper code blocks.


License
-------

BSD 2-clause simplified. See ``LICENSE``.
