
from Things import *
import re

####    ####    ####    ####    ####    ####    ####    ####    

# EMPTY = Unique()
# QUOTE = Unique()

####    ####    ####    ####    ####    ####    ####    ####    

tokens = (
	'STRING',
	# 'HASH',
	# 'COMMA',
	'LPAREN', 
	'RPAREN',
	'LSQUARE', 
	'RSQUARE',
	# 'LQUOTE',
	# 'RQUOTE',
	'NUM',
	'SYM',
	'CONST',
	)

# Tokens
t_STRING    = r'\"[^\"]*\"'
# t_HASH		= r'\#'
# t_COMMA     = r','
t_LPAREN	= r'\('
t_RPAREN	= r'\)'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
# t_LQUOTE	= r'`'
# t_RQUOTE	= r'\''
t_NUM		= r'\d[^\"\#,`\(\)\[\]`\s@]*'	# TODO: negative numbers
t_SYM       = r'[^\"\#,`\(\)\[\]`\s\d@][^\"\#,`\(\)\[\]`\s@]*'
t_CONST     = r'@[^\"\#,`\(\)\[\]`\s@]*'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")
	
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# lexer.input("hey you ,'(wat no hey) [wat]")
# while True:
# 	tok = lexer.token()
# 	if not tok: break      # No more input
# 	print tok

####	####	####	####	####	####	####	####	

def p_statement_term(t):
	'''statement : term'''
	t[0] = t[1]

def p_term_sym(t):
	'''term : SYM'''
	t[0] = Symbol(t[1])
def p_term_num(t):
	'''term : NUM'''
	try:		t[0] = int(t[1])
	except:		
		try:	t[0] = float(t[1])
		except: t[0] = 0
def p_term_string(t):
	'''term : STRING'''
	t[0] = t[1][1:-1]
def p_term_const(t):
	'''term : CONST'''
	t[0] = CONSTS[t[1]]


def p_term_appr(t):
	'''term : LPAREN list RPAREN'''
	t[0] = Expr([APP]+t[2])
def p_term_expr(t):
	'''term : LSQUARE list RSQUARE'''
	t[0] = Expr(t[2])
def p_list(t):
	'''list : term list
			| term'''
	t[0] = t[2] if len(t) == 3 else []
	t[0].insert(0, t[1])

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

####	####	####	####	####	####	####	####	


def chopLine(s):
    ind = re.search(r'##|#!', s)
    return s[:ind.start()] if ind >= 0 else s

def removeCommentLines(s):
    return '\n'.join([chopLine(line) for line in s.splitlines()])

def parse(s):
    # s = "#(0)\n"+removeCommentLines(s)  # hack because can't parse empty file....
    s = removeCommentLines(s)
    return parser.parse(s)

# def parse1(s): return parse(s)[0]

# print parse("f(4, f[4], `hi) ## comment")
# print parse("f(4, f[4], `hi', @T, @E, moo, 45, \"lol\") ## comment")

# print parse("(1 2 3 #)")

# print parse("(abc = (* 2 'th ree' \"two\") in (+ \"1\" abc)) test : (1 2 3)")
# print parse("hey : (abc = (* 2 'th ree' \"two\") in (+ \"1\" abc)) test : (1 2 3)")
# print parse("hey : (abc = (* 2 'th ree' \"two\") in (+ \"1\" abc))")
# print parse("hey : you [wat : no hey] wat")

# __all__ = ["parse", "AST", "GVR"]




