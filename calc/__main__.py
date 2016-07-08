'''
The MIT License (MIT)

Copyright (c) 2016 Jacob McGladdery

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from calc import CalcParser
from grako.exceptions import FailedParse
from decimal import Decimal

__version__ = '1.0.1'


class CalcSemantics:

    def expression(self, ast):
        result = ast.head
        for node in ast.tail:
            op = node[0]
            rhs = node[1]
            if '+' == op:
                result += rhs
            elif '-' == op:
                result -= rhs
        return result

    def term(self, ast):
        result = ast.head
        for node in ast.tail:
            op = node[0]
            rhs = node[1]
            if '*' == op:
                result *= rhs
            elif '/' == op:
                result /= rhs
        return result

    def power(self, ast):
        result = ast.head
        for node in ast.tail:
            result = result ** node[1]
        return result

    def factor(self, ast):
        return ast

    def negative(self, ast):
        return -ast

    def number(self, ast):
        return Decimal(ast)


def main():
    print('Welcome to Calc v{}'.format(__version__))
    try:
        parser = CalcParser(semantics=CalcSemantics())
        while True:
            try:
                text = input('> ')
                if text:
                    print(parser.parse(text))
            except FailedParse:
                print('Invalid syntax')
    except EOFError:
        pass
    except KeyboardInterrupt:
        print()
    print('Bye')

if __name__ == '__main__':
    main()
