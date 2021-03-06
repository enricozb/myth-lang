import builtins
import utils

from contextlib import contextmanager
from functools import reduce, partial
from myth_lex import tokens
from pprint import pprint

precedence = (
    ('left', 'RPAREN_MAPSTO', 'MAPSTO'),
    ('left', 'OPERATOR'),
    ('left', 'BAR'),
)

class DictStack:
    def __init__(self, names):
        self.dicts = [names]

    @contextmanager
    def push(self, names):
        self.dicts.append(names)
        yield
        self.pop()

    def pop(self):
        self.dicts.pop()

    def update(self, d):
        self.dicts[-1].update(d)

    def __getitem__(self, key):
        for d in self.dicts[::-1]:
            if key in d:
                return d[key]
        raise Exception(f"Variable '{key}' not in scope")

    def __setitem__(self, key, val):
        self.dicts[-1][key] = val


names = DictStack(
    {name: func for name, func in vars(builtins).items()
        if not name.startswith('__')}
)
names.update({'reduce': reduce, 'partial': partial})
import operator

class BuiltinFunc:
    def __init__(self, f, name, num_params):
        self.f = f
        self.name = name
        self.min_params, self.max_params = num_params

    def __call__(self, *params):
        if self.min_params <= len(params) <= self.max_params:
            return self.f(*params)
        raise TypeError(
            f'{self.name} takes from {self.min_params} to {self.max_params} '
            f'positional arguments but {len(params)} were given'
        )

    def __repr__(self):
        return f'<built-in function {self.name}>'


names['+'] = BuiltinFunc(lambda a, b=None: a + b if b else a, 'add', (1, 2))
names['-'] = BuiltinFunc(lambda a, b=None: a - b if b else -a, 'sub', (1, 2))
names['*'] = operator.mul
names['/'] = operator.truediv
names['//'] = operator.floordiv
names['^'] = operator.pow
names['='] = operator.eq

names['in'] = lambda a, b: a in b
names['or'] = lambda a, b: a or b
names['and'] = lambda a, b: a and b
names['not'] = operator.__not__

def lambda_literal(capturelist, expression):
    def func(*args):
        expected, received = len(capturelist), len(args)
        if len(args) != len(capturelist):
            raise Exception(
                f'lambda expected {expected} argument{"s" * (expected > 1)} '
                f'but got {received}'
            )

        received_args = dict(zip(capturelist, args))
        with names.push({**func.bound_args, **received_args}):
            val = eval_bytecode(expression)
            if callable(val):
                val.bound_args = {**func.bound_args, **received_args}

        return val

    func.bound_args = {}
    return func

def eval_bytecode(code):
    instr, *args = code
    if instr == 'assign':
        names[args[1]] = eval_bytecode(args[0])
    elif instr == 'call':
        return eval_bytecode(args[0])(*map(eval_bytecode, args[1]))
    elif instr == 'literal':
        if type(args[0]) in (list, set):
            return type(args[0])(map(eval_bytecode, args[0]))
        return args[0]
    elif instr == 'name':
        return names[args[0]]
    elif instr == 'conditional':
        for condition, expression in zip(args[0], args[1]):
            if eval_bytecode(condition):
                return eval_bytecode(expression)

def p_statment(t):
    """
    statement : assign
              | expression
    """
    if builtins.verbose > 0:
        print('Verbose:', utils.prefix_format(t[1]))
    val = eval_bytecode(t[1])
    if val is not None:
        print(repr(val))
        names['_'] = val

def p_arglist(t):
    """
    arglist : expression
            | arglist COMMA expression
    """
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_name(t):
    """
    name : OPERATOR
         | NAME
    """
    t[0] = t[1]

def p_call_name(t):
    """
    call : name LPAREN RPAREN
         | name LPAREN arglist RPAREN
    """
    if len(t) == 4:
        t[0] = ('call', ('name', t[1]), [])
    else:
        t[0] = ('call', ('name', t[1]), t[3])

def p_call_expression(t):
    """
    call : LPAREN expression RPAREN LPAREN RPAREN
         | LPAREN expression RPAREN LPAREN arglist RPAREN
    """
    t[0] = ('call', t[2], [] if len(t) == 6 else t[5])

def p_call_curried(t):
    """
    call : call LPAREN RPAREN
         | call LPAREN arglist RPAREN
    """
    t[0] = ('call', t[1], [] if len(t) == 4 else t[3])

def p_assign(t):
    """
    assign : name COLON expression
    """
    t[0] = ('assign', t[3], t[1])

def p_expression_name(t):
    """
    expression : name
    """
    t[0] = ('name', t[1])

def p_expression(t):
    """
    expression : operator_invocation
               | conditional
               | call
               | literal
               | LPAREN expression RPAREN
    """
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]

def p_conditional(t):
    """
    conditional : BAR LPAREN expression RPAREN_MAPSTO expression
                | conditional BAR LPAREN expression RPAREN_MAPSTO expression
    """
    if len(t) == 6:
        t[0] = ('conditional', [t[3]], [t[5]])
    else:
        t[0] = ('conditional', t[1][1] + [t[4]], t[1][2] + [t[6]])

def p_literal(t):
    """
    literal : NUMBER
            | list
            | set
            | lambda
            | STRING
    """
    t[0] = ('literal', t[1])

def p_set(t):
    """
    set : LBRACE arglist RBRACE
        | LBRACE RBRACE
    """
    if len(t) == 3:
        t[0] = set()
    else:
        t[0] = set(t[2])

def p_list(t):
    """
    list : LBRACKET arglist RBRACKET
         | LBRACKET RBRACKET
    """
    if len(t) == 3:
        t[0] = []
    else:
        t[0] = t[2]

def p_lambda(t):
    """
    lambda : NAME MAPSTO expression
           | LPAREN capture_list RPAREN_MAPSTO expression
    """
    if len(t) == 4:
        t[0] = lambda_literal([t[1]], t[3])
    else:
        t[0] = lambda_literal(t[2], t[4])

def p_capture_list(t):
    """
    capture_list : name
                 | capture_list COMMA name
    """
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_operator_invocation(t):
    """
    operator_invocation : operator_invocation_postfix
                        | operator_invocation_prefix
                        | operator_invocation_infix
    """
    t[0] = t[1]

def p_operator_invocation_infix(t):
    """
    operator_invocation_infix : expression OPERATOR expression
    """
    t[0] = ('call', ('name', t[2]), [t[1], t[3]])

def p_operator_invocation_postfix(t):
    """
    operator_invocation_postfix : expression OPERATOR
    """
    t[0] = ('call', ('name', t[2]), [t[1]])

def p_operator_invocation_prefix(t):
    """
    operator_invocation_prefix : OPERATOR expression
    """
    t[0] = ('call', ('name', t[1]), [t[2]])


def p_error(t):
    val = f" at '{t.value}' on line {t.lexer.lineno}" if t else ''
    raise Exception(f"Syntax error{val}")

import ply.yacc as yacc
parser = yacc.yacc()
