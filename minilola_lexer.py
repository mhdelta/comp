import ply.lex as lex
import sys

# list of tokens
# fOR LoLa
tokens = (
    # Reserverd words
    #'AUTO',
    'ARRAY',
    'BEGIN',
    'BIT',
    'BOOLEAN',
    'CASE',
    'CHAR',
    'CONST', 
    'DO',
    'ELSE',
    'ELSEIF',
    'END',
    'EXIT',
    'FALSE',
    'FOR',
    'IF',
    'IMPORT',
    'IN',
    'INOUT',
    'INTEGER',
    'IS',
    'LONG',
    'LONGINT',
    'LOOP',
    'MOD',
    'MODULE',
    'NIL',
    'OF',
    'OUT',
    'PROCEDURE',
    'REG',
    'REPEAT',
    'SHORT',
    'SHORTINT',
    'STRING',
    'THEN',
    'TO',
    'TRUE',
    'TS',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'WORD',
       
    # Symbols
    'AMPERSANT',
    'APOSTROF',
    'ARROW',
    'ASSIGN',
    'CIRCUNFLEX',
    'COLON',
    'COMMA',
    'DEQUAL',
    'DEQUAL',
    'DISTINT',
    'DOT',
    'EQUAL',
    'GREATER',
    'GREATEREQUAL',
    'HASHTAG',
    'LBLOCK',
    'LBRACKET',
    'LESS',
    'LESSEQUAL',
    'LPAREN',
    'MINUS',
    'NEGATION',
    'PLUS',
    'RBLOCK',
    'RBRACKET',
    'RPAREN',
    'SEMICOLON',
	'TIMES',

    # Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens 
t_AMPERSANT = r'\&'
t_APOSTROF = r"'"
t_ARROW = r'->'
t_ASSIGN = r':='
t_CIRCUNFLEX = r'\^'
t_COLON   = r':'
t_COMMA  = r','
t_DISTINT = r'!'
t_DOT = r'\.'
t_EQUAL  = r'='
t_GREATER = r'>'
t_HASHTAG = r'\#'
t_LBLOCK   = r'{'
t_LBRACKET = r'\['
t_LESS   = r'<'
t_LPAREN = r'\('
t_MINUS  = r'-'
t_NEGATION = r'~'
t_PLUS   = r'\+'
t_RBLOCK   = r'}'
t_RBRACKET = r'\]'
t_RPAREN  = r'\)'
t_SEMICOLON = ';'
t_TIMES  = r'\*'

def t_ARRAY(t):
    r'ARRAY'
    return t

def t_BEGIN(t):
    r'BEGIN'
    return t

def t_BIT(t):
    r'BIT'
    return t

def t_BOOLEAN(t):
    r'BOOLEAN'
    return t

def t_CASE(t):
    r'CASE'
    return t

def t_CHAR(t):
    r'CHAR'
    return t

def t_DO(t):
    r'DO'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_ELSEIF(t):
    r'ELSEIF'
    return t

def t_END(t):
    r'END'
    return t

def t_EXIT(t):
    r'EXIT'
    return t

def t_FOR(t):
    r'FOR'
    return t

def t_IF(t):
    r'IF'
    return t

def t_IMPORT(t):
    r'IMPORT'
    return t

def t_IN(t):
	r'IN'
	return t

def t_INOUT(t):
    r'INOUT'
    return t

def t_INTEGER(t):
    r'INTEGER'
    return t

def t_IS(t):
    r'IS'
    return t

def t_LONG(t):
    r'LONG'
    return t

def t_LONGINT(t):
    r'LONGINT'
    return t

def t_LOOP(t):
    r'LOOP'
    return t

def t_MODULE(t):
    r'MODULE'
    return t

def t_MOD(t):
    r'MOD'
    return t


def t_NIL(t):
    r'NIL'
    return t

def t_OF(t):
    r'OF'
    return t

def t_OUT(t):
    r'OUT'
    return t

def t_PROCEDURE(t):
    r'PROCEDURE'
    return t

def t_REG(t):
    r'REG'
    return t

def t_REPEAT(t):
    r'REPEAT'
    return t

def t_SHORT(t):
    r'SHORT'
    return t

def t_SHORTINT(t):
    r'SHORTINT'
    return t

def t_STRING(t):
    r'"(.)+"'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_TO(t):
    r'TO'
    return t

def t_TRUE(t):
    r'TRUE'
    return t

def t_FALSE(t):
    r'FALSE'
    return t

def t_TS(t):
    r'TS'
    return t

def t_TYPE(t):
    r'TYPE'
    return t

def t_UNTIL(t):
    r'UNTIL'
    return t

def t_VAR(t):
    r'VAR'
    return t

	
def t_WHILE(t):
	r'WHILE'
	return t

def t_WORD(t):
    r'WORD'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'[(][*](.|\n)*?[*][)]'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Evaluaciones/evaluacion.lola'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
