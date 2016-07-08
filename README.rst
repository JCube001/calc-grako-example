Grako Calculator Example
========================

The official Grako package lacks a "Hello, World!" example detailing how to
correctly use the Grako tool with both operator precedence and custom semantic
actions. This package provides such an example. Specifically this package is
an infix math expression REPL application.

For more information about the PEG parser generator Grako, see the `PyPI page
<https://pypi.python.org/pypi/grako>`_.


Install
-------

No installation is required since this application can be run using ``python
/path/to/calc``. This will execute __main__.py automatically. If you choose to
run the application this way, then you will need to run ``pip install grako``
first.

The Calc package can also be installed using ``pip install /path/to/calc``.
Installing this way will automatically take care of any dependencies.


Usage
-----

If you wish to run the calc application without installing, then run ``python
/path/to/calc``. If you installed calc using pip, then simply invoke ``calc``
from the command line.

After the ``>`` prompt appears, you may then type a math expression as a
sequence of decimal numbers and operators. Press enter to have the expression
evaluated. The result will print immediately on the following line. Another
prompt will then appear. Use Ctrl+C or type your system's EOF character in
order to exit calc.

The calc application recognizes the following operators:

+-----------+----------------+
| Operator  | Description    |
+===========+================+
| ``( x )`` | Grouping       |
+-----------+----------------+
| ``^``     | Exponentiation |
+-----------+----------------+
| ``*``     | Multiplication |
+-----------+----------------+
| ``/``     | Division       |
+-----------+----------------+
| ``+``     | Addition       |
+-----------+----------------+
| ``-``     | Subtraction    |
+-----------+----------------+


How It Works
------------

- Operator precedence is achieved by encoding it within the EBNF grammar.
- Lower precedence operators appear first.
- Operators with the same level of precedence appear together in the same
  grammar rule.
- Binary operators are specified as an optional list. This makes it trivial to
  reduce the AST for a given expression to just a single value within the
  semantic action.
- Higher precedence operators must be resolved by the parser by it recusing
  through the lower precedence grammar rules which come before it. This results
  in an AST where the higher precedence expressions appear lower in the tree.
  This means the expressions which contain a higher precedence operator will be
  evaluated before all others.
