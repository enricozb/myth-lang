# Myth
Just a toy language -- Learning how to use PLY/yacc

## How to use
Myth currently only has an interpreter mode, and can be run by executing

    python3 myth.py

## Example Syntax
### Literals and Assignment
Assignment is done by `name: expr`, where `name` will take the value of `expr`.
For example,

    a: 1
    b: True
    c: "Hello"
    d: [1, 2, 3]
    e: {1, 2, 3}

For clarity, `d` is a list and `e` is a set. Python dictionary syntax is not
supported, and currently list/string element access does not exist.

### Math
Standard math operators are included in the language:

    1 + 1  # -> 2   (addition)
    1 - 1  # -> 0   (subtraction)
    2 * 2  # -> 4   (multiplication)
    9 / 3  # -> 3.0 (real division)
    3 ^ 2  # -> 9   (exponentiation)
    3 // 2 # -> 1   (integer division)

Boolean operators/literals are identical to those in Python.

    not False       # -> True
    True or False   # -> True

### Functions
Myth is tightly coupled with Python, and has access to all of the Python
global builtin functions.

    sum([1, 2, 3])    # -> 6
    sum(range(100))   # -> 4950

Lambdas have a syntax slightly different than Python's.

    increment: x -> x + 1
    add: (x, y) -> x + y

Calling functions, as we've seen above, is very similar to Python's syntax.

### Operators
Operators are interesting in Myth, they are almost exactly like variable names.
The only difference is that they can be infixed/prefixed/postfixed as a function
call. For example,

    1 + 1
    # is the same as
    +(1, 1)

This also means they can be created, assigned to, and passed as parameters.

    myth> ++: partial(+, 1)
    myth> 1++
    2
    myth> ++1
    2

Operators can only contain a special set of characters, see `myth_lex.py` for the
specific character set.
