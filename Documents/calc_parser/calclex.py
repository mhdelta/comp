# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import sys 
from Tkinter import Tk
from tkFileDialog import askopenfilename
from termcolor import colored

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def test(data, lexer):
  lexer.input(data)
  while True:
    tok = lexer.token()
    if not tok:
      break
    print (tok) 

 
if __name__ == '__main__':
  if (len(sys.argv) > 1):
    fin = sys.argv[1]
  else:
    Tk().withdraw()
    filename = "test.txt"
  f = open(filename, 'r')
  data = f.read()
  print colored(data, 'green')
  lexer.input(data)
  test(data, lexer)
  input()