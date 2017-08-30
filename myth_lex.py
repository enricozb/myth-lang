from ast import literal_eval

tokens = (
    'NAME', 'NUMBER', 'COLON', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE', 'COMMA', 'MAPSTO', 'RPAREN_MAPSTO', 'OPERATOR',
    'STRING', 'BAR',
)

t_ignore = ' '

t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_BAR = r'\|'

reserved = {
    'in' : 'OPERATOR',
    'or' : 'OPERATOR',
    'not' : 'OPERATOR',
}

def t_NAME(t):
    r'[a-zA-Z_]+'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'L?\"(.|[^\"])*\"'
    t.value = literal_eval(t.value)
    return t

def t_RPAREN_MAPSTO(t):
    r'\)\s+->'
    return t

def t_MAPSTO(t):
    r'->'
    return t

def t_OPERATOR(t):
    r'''[\+\-\*\/\^=\']+'''
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print('Illegal character {}'.format(t.value[0]))
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()