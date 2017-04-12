import ply.yacc as yacc
import os
import codecs
import re
import sys
from minilola_lexer import tokens
import minilola_lexer
from sys import stdin 



precedence =(
('right', 'ASSIGN'),




)

def P_program(p):
	'''program = block'''
	print "program"
	#p[0] =  program(p[1], "Program")

def P_block(p):
	'''block : constDecl'''
	print "constDecl"

def p_constDecl(p):
	'''constDecl: CONST constAssignmentList ;'''
	print"constDecl"

def constAssignmentList(p):
	'''constAssignmentList : constAssignmentList, ID = NUMBER'''
	print"constAssignmentList 1"



parser=yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.c'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")
	#input()
