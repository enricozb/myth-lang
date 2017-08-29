tokens = (
    'NAME', 'NUMBER', 'COLON', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE', 'COMMA', 'MAPSTO', 'RPAREN_MAPSTO', 'OPERATOR'
)

t_ignore = ' '

t_NAME = r'[a-zA-Z_]+'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_MAPSTO = r'->'
t_RPAREN_MAPSTO = r'\)\s+->'
t_OPERATOR = r'[\+\-\*\/\^]+'

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