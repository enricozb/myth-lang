import builtins

from functools import reduce, partial
from myth_lex import tokens
from pprint import pprint

precedence = (
    ('left', 'RPAREN_MAPSTO', 'MAPSTO'),
    ('left', 'OPERATOR'),
)

class DictStack:
    def __init__(self, names):
        self.dicts = [names]

    def push(self, names):
        self.dicts.append(names)

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

names['+'] = operator.add
names['-'] = operator.sub
names['*'] = operator.mul
names['/'] = operator.truediv
names['//'] = operator.floordiv
names['^'] = operator.pow

def lambda_literal(capturelist, expression):
    def func(*args):
        expected, received = len(capturelist), len(args)
        if len(args) != len(capturelist):
            raise Exception(
                f'lambda expected {expected} argument{"s" * (expected > 1)} '
                f'but got {received}'
            )

        names.push(dict(zip(capturelist, args)))
        val = eval_bytecode(expression)
        names.pop()
        return val

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

def p_statment(t):
    """
    statement : assign
              | expression
    """
    if builtins.verbose:
        pprint(t[1])
    val = eval_bytecode(t[1])
    if val is not None:
        print(val)
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
    call : name LPAREN arglist RPAREN
    """
    t[0] = ('call', ('name', t[1]), t[3])

def p_call_expression(t):
    """
    call : LPAREN expression RPAREN LPAREN arglist RPAREN
    """
    t[0] = ('call', t[2], t[5])

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
               | call
               | literal
               | LPAREN expression RPAREN
    """
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]

def p_literal_number(t):
    """
    literal : NUMBER
            | list
            | set
            | lambda
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
    lambda : name MAPSTO expression
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
    operator_invocation : expression OPERATOR expression
    """
    t[0] = ('call', ('name', t[2]), [t[1], t[3]])


def p_error(t):
    val = f" at '{t.value}'" if t else ''
    raise Exception(f"Syntax error{val}")

import ply.yacc as yacc
parser = yacc.yacc()
