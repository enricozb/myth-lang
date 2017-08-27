import readline

tokens = (
    'NAME', 'NUMBER', 'COLON', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'COMMA', 'MAPSTO'
)

t_ignore = ' '

t_NAME = r'[a-zA-Z_]+'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_MAPSTO = r'->'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print('Illegal character {}'.format(t.value[0]))
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

class DictStack:
    def __init__(self, names):
        self.dicts = [names]

    def push(self, names):
        self.dicts.append(names)

    def pop(self):
        self.dicts.pop()

    def __getitem__(self, key):
        for d in self.dicts[::-1]:
            if key in d:
                return d[key]
        raise Exception(f"Variable '{key}' not in scope")

    def __setitem__(self, key, val):
        self.dicts[-1][key] = val

names = DictStack(locals()['__builtins__'].__dict__)

def lambda_literal(capturelist, expression):
    def func(*args):
        assert len(args) == len(capturelist)
        args = {name : var for name, var in zip(capturelist, args)}
        names.push(args)
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
        return args[0]
    elif instr == 'name':
        return names[args[0]]

def p_statment(t):
    """
    statement : assign
              | expression
    """
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

def p_call_name(t):
    """
    call : NAME LPAREN arglist RPAREN
    """
    t[0] = ('call', ('name', t[1]), t[3])

def p_call_expression(t):
    """
    call : LPAREN expression RPAREN LPAREN arglist RPAREN
    """
    t[0] = ('call', t[2], t[5])

def p_assign(t):
    """
    assign : NAME COLON expression
    """
    t[0] = ('assign', t[3], t[1])

def p_expression_name(t):
    """
    expression : NAME
    """
    t[0] = ('name', t[1])

def p_expression(t):
    """
    expression : call
               | literal
    """
    t[0] = t[1]

def p_literal_number(t):
    """
    literal : NUMBER
            | list
            | lambda
    """
    t[0] = ('literal', t[1])

def p_list(t):
    """
    list : LBRACKET arglist RBRACKET
         | LBRACKET RBRACKET
    """
    if len(t) == 3:
        t[0] = []
    else:
        t[0] = list(map(eval_bytecode, t[2]))

def p_lambda_singlearg(t):
    """
    lambda : NAME MAPSTO expression
           | LPAREN NAME RPAREN MAPSTO expression
    """
    if len(t) == 4:
        t[0] = lambda_literal([t[1]], t[3])
    else:
        t[0] = lambda_literal([t[2]], t[5])

def p_lambda(t):
    """
    lambda : LPAREN arglist RPAREN MAPSTO expression
    """
    if not all(map(lambda x: x[0] == 'name', t[2])):
        raise SyntaxError('Wat')
    t[0] = lambda_literal([name for _, name in t[2]], t[5])


def p_error(t):
    val = f" at '{t.value}'" if t else ''
    raise Exception(f"Syntax error{val}")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('myth> ')
        yacc.parse(s)
    except EOFError:
        break
    except Exception as e:
        print(e)
