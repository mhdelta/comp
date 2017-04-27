import ply.yacc as yacc
from minilola_lexer import tokens
import minilola_lexer
import sys

VERBOSE = 1



def p_Module(p):
	''' Module : MODULE	ID SEMICOLON module1 module2 module3 module4 module5 module6 module7 END ID DOT'''
	pass

def p_TypeDeclaration(p):
	''' TypeDeclaration : TYPE ID times1 typedeclaration1 SEMICOLON module2 typedecl3 typedecl4 module5 module6 module7 END ID'''
	pass



def p_SimpleType(p):
	'''SimpleType : BasicType
			| ID  [ 'LPAREN ExpressionList RPAREN' ]'''
	pass

# def p_simpletype1(p):
# 	'''simpletype1 : empty
# 		| LPAREN ExpressionList RPAREN'''
# 	pass

def p_BasicType(p):
	'''BasicType :	BIT
			| TS 
			| OC ''' 
	pass	

def p_ExpressionList(p):
	'''ExpressionList : Expression expressionlist1'''
	pass

def p_expressionlist1(p):
	'''expressionlist1 : empty
		| expressionlist1 COMMA Expression ''' 
	pass


def p_type(p):
	'''Type : type1 SimpleType''' 
	pass

def p_type1(p):
	''' type1 : empty
		| type1 RBRACKET Expression LBRACKET'''
	pass 

def p_ConstDeclaration(p):
	'''ConstDeclaration : ID ASSIGN Expression SEMICOLON'''
	pass

def p_VarDeclaration(p):
	'''VarDeclaration : IdList COLON Type SEMICOLON'''
	pass

def p_IdList(p):
	'''IdList : ID idlist1'''
	pass

def p_idlist1(p):
	'''idlist1 : empty
		| idlist1 COMMA ID'''
	pass 

def p_Selector(p):
	''' Selector : selector1'''
	pass

def p_selector1(p):
	''' selector1 : empty
		| selector1 DOT ID
		| selector1 DOT INTEGER
		| selector1 LBRACKET Expression RBRACKET'''
	pass

def p_Factor(p):
	'''Factor : ID Selector
		| LOGIC0
		| LOGIC1
		| INTEGER
		| NEGATION Factor
		| LPAREN Expression RPAREN
		| MUX LPAREN Expression COLON Expression COMMA Expression RPAREN 
		| MUX LPAREN Expression COMMA Expression COLON Expression COMMA Expression COMMA Expression COMMA Expression RPAREN
		| REG LPAREN ExpressionList RPAREN
		| LATCH LPAREN LPAREN Expression COMMA Expression RPAREN 
		| SR LPAREN Expression COMMA Expression RPAREN '''
	pass

def p_Term(p):
	''' Term : Factor term1'''
	pass

def p_term1(p):
	''' term1 : empty
		| term1 term2 Factor'''
	pass

def p_term2(p):
	''' term2 : TIMES
		| DIVISION
		| DIV
		| MOD '''
	pass


def p_Expression(p):
	'''Expression : Term expression1'''
	pass

def p_expression1(p):
	''' expression1 : empty
		| expression1 expression2 Term'''
	pass

def p_expression2(p):
	''' expression2 : PLUS
		| MINUS  '''
	pass

def p_Assignment(p):
	''' Assignment : ID Selector ASSIGN assignment1 Expression'''	
	pass

def p_assignment1(p):
	''' assignment1 : empty
		| Condition OR '''

def p_Condition(p):
	' Condition : Expression'
	pass	

def p_Relation(p):
	'''Relation : Expression "=" Expression
		| Expression HASHTAG Expression
		| Expression LESS Expression
		| Expression LESSEQUAL Expression
		| Expression GREATER Expression
		| Expression GREATEREQUAL Expression'''
	pass

def p_IfStatement(p):
	''' IfStatement : IF Relation THEN StatementSequence ifstatement1 ifstatement2 END''' 
	pass

def p_ifstatement1(p):
	''' ifstatement1 : empty
		| ifstatement1 ELSIF Relation THEN StatementSequence '''
	pass
	
def p_ifstatement2(p):
	''' ifstatement2 : empty
		| ELSE StatementSequence'''	

def p_ForStatement(p):
	''' ForStatement : FOR ID ASSIGN Expression DOTDOT Expression DO StatementSequence END
		| ELSIF Relation THEN StatementSequence
		| ELSE StatementSequence
		| END''' 
	pass

def p_Statement(p):
	''' Statement : Assignment
		| UnitAssignment
		| IfStatement
		| ForStatement '''
	pass



def p_StatementSequence(p):
	''' StatementSequence : Statement statementsequence1 '''
	pass

def p_statementsequence1(p):
	''' statementsequence1 : empty
		| statementsequence1 SEMICOLON Statement'''	
	pass



def p_times1(p):
	''' times1 : empty
		| TIMES'''
	pass

def p_typedeclaration1(p):
	''' typedeclaration1 : empty
		| LPAREN IdList RPAREN'''
	pass

def p_typedecl3(p):
	''' typedecl3 : empty
		| IN typedecl31'''
	pass

def p_typedecl31(p):
	''' typedecl31 : empty
		| typedecl31 IdList COLON FormalType SEMICOLON'''
	pass

def p_typedecl4(p):
	''' typedecl4 : empty
		| IN typedecl41'''
	pass

def p_typedecl41(p):
	''' typedecl41 : empty
		| typedecl41 IdList COLON FormalBusType SEMICOLON'''
	pass

def p_module1(p):
	''' module1 : empty
		| module1 TypeDeclaration SEMICOLON'''
	print "flag mod 1"
	pass

def p_module2(p):
	''' module2 : CONST module21
		| empty'''
	print"flag mod 2"
	pass

def p_module21(p):
	''' module21 : ConstDeclaration
		| empty '''
	print"flag mod 21"
	pass

def p_module3(p):
	''' module3 : empty
		| IN module31'''
	pass

def p_module31(p):
	''' module31 : empty
		| module31 VarDeclaration'''
	pass

def p_module4(p):
	''' module4 : empty
		| INOUT module41'''
	pass

def p_module41(p):
	''' module41 : empty
		| module41 VarDeclaration'''
	pass

def p_module5(p):
	''' module5 : empty
		| OUT module51'''
	pass

def p_module51(p):
	''' module51 : empty
		| module51 VarDeclaration'''
	pass

def p_module6(p):
	''' module6 : empty
		| VAR module61'''
	pass

def p_module61(p):
	''' module61 : empty
		| module61 VarDeclaration'''
	pass

def p_module7(p):
	''' module7 : empty
		|  BEGIN StatementSequence'''
	pass

def p_FormalType(p):
	''' FormalType : formaltype1 BIT'''
	pass

def p_formaltype1(p):
	''' formaltype1 : empty
		| formaltype1
		| LBRACKET formaltype2 RBRACKET'''
	pass

def p_formaltype2(p):
	''' formaltype2 : empty
		| Expression'''
	pass

def p_FormalBusType(p):
	''' FormalBusType : formaltype1 tsoroc'''
	pass

def p_tsoroc(p):
	''' tsoroc : TS
		| OC'''
	pass



def p_UnitAssignment(p):
	'UnitAssignment : ID Selector LPAREN ExpressionList RPAREN'
	pass 




def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')



parser=yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Evaluaciones/evaluacion.lola'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")
	#input()ctor
