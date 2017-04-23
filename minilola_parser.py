import ply.yacc as yacc
from minilola_lexer import tokens
import minilola_lexer
import sys

VERBOSE = 1

def p_LogicValue(p):
	'''LogicValue :	"'" "0"
			| "'" "1" ''' 
	pass	

def p_SimpleType(p):
	'''SimpleType : BasicType
			| ID "(" ExpressionList ")" '''
	pass
def p_BasicType(p):
	'''BasicType :	BIT
			| TS ''' 
	pass	

def p_ExpressionList(p):
	'''ExpressionList : Expression ExpressionList
			| "," Expression 
			|  empty'''
	pass


def p_type(p):
	'''Type : SimpleType
		| "[" Expression "]" SimpleType''' 
	pass

def p_ConstDeclaration(p):
	'''ConstDeclaration : ID ASSIGN Expression ";"
		| empty '''
	pass

def p_VarDeclaration(p):
	'''VarDeclaration : IdList ":" Type ";"
		| empty'''
	pass

def p_IdList(p):
	'''IdList : ID IdList
			| "," ID 
			| empty'''
	pass

def p_Selector(p):
	''' Selector : "." ID
		| "." INTEGER 
		| "[" Expression "]"
		| empty'''
	pass

def p_Factor(p):
	'''Factor : ID Selector
		| LogicValue
		| INTEGER
		| "~" Factor
		| "(" Expression ")"
		| MUX "(" Expression ":" Expression "," Expression ")" 
		| MUX "(" Expression "," Expression ":" Expression "," Expression "," Expression "," Expression ")"
		| REG "(" ExpressionList ")"
		| LATCH "(" "(" Expression "," Expression ")" 
		| SR "(" Expression "," Expression ")" '''
	pass

def p_Term(p):
	''' Term : Factor Term
		| "*" Factor Term
		| "/" Factor Term
		| DIV Factor Term
		| MOD Factor Term
		| empty'''
	pass	


def p_Expression(p):
	'''Expression : Term Expression
		| "+" Term
		| "-" Term
		| empty '''
	pass

def p_Assignment(p):
	''' Assignment : ID Selector ASSIGN Assignment Expression
		| Condition "|" 
		| empty'''
	pass

def p_Condition(p):
	' Condition : Expression'
	pass	

def p_Relation(p):
	'''Relation : Expression "=" Expression
		| Expression "#" Expression
		| Expression "<" Expression
		| Expression LESSEQUAL Expression
		| Expression ">" Expression
		| Expression GREATEREQUAL Expression'''
	pass

def p_IfStatement(p):
	''' IfStatement : IF Relation THEN StatementSequence IfStatement
		| ELSIF Relation THEN StatementSequence
		| ELSE StatementSequence
		| END
		| empty''' 
	pass

def p_ForStatement(p):
	''' ForStatement : FOR ID ASSIGN Expression DOTDOT Expression DO StatementSequence END
		| ELSIF Relation THEN StatementSequence
		| ELSE StatementSequence
		| END
		| empty''' 
	pass

def p_Statement(p):
	''' Statement : Assignment
		| UnitAssignment
		| IfStatement
		| ForStatement '''
	pass

def p_StatementSequence(p):
	''' StatementSequence : Statement StatementSequence
		| ";" Statement
		| empty '''
	pass

def p_Module(p):
	''' Module : MODULE	ID ";" Module END ID "."
		| TypeDeclaration ";"
		| CONST ConstDeclaration
		| IN VarDeclaration
		| INOUT VarDeclaration
		| OUT VarDeclaration
		| VAR VarDeclaration
		| BEGIN StatementSequence
		| empty'''
	pass

def p_FormalType(p):
	''' FormalType : FormalType BIT
		| "[" Expression "]"
		| empty'''
	pass

def p_FormalBusType(p):
	''' FormalBusType : FormalBusType TS
		| "[" Expression "]"
		| empty'''
	pass

def p_TypeDeclaration(p):
	''' TypeDeclaration : TYPE ID "*" TypeDeclaration ";" END
		| CONST ConstDeclaration
		| IN "(" IdList ")" ":" FormalType 
		| OUT VarDeclaration
		| VAR VarDeclaration
		| BEGIN StatementSequence
		| empty'''
	pass

def p_UnitAssignment(p):
	'UnitAssignment : ID Selector "(" ExpressionList ")"'
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
