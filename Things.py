
from collections import namedtuple
from Disp import *
import operator as op

####    ####    ####    ####    ####    ####    ####    ####    

class Expr(tuple):
	def __repr__(self): 
		if self[0] == APP: return "("+" ".join(map(repr, self[1:]))+")"
		else: return "["+" ".join(map(repr, self))+"]"
class Symbol(str):
	def __repr__(self): return self
class Unique(): 
	def __init__(self, name): self.name = name
	def __repr__(self): return self.name
class Closure(namedtuple('Closure', ['args', 'body', 'nv'])):
	def __repr__(self): 
		return "[@lamb "+" ".join(map(repr, self.args))+" "+repr(self.body)+"]"
class Function(namedtuple('Function', ['name', 'args', 'body', 'nv'])):
	def __repr__(self): 
		return "[@func "+self.name+" "+" ".join(map(repr, self.args))+" "+repr(self.body)+"]"
class Env(object):
	def __init__(self, d, nv): self.d, self.nv = d, nv
	def __getitem__(self, key):
		return self.d[key] if key in self.d else self.nv[key]

APP = Unique("@app")
LET = Unique("@let")
LAMB = Unique("@lamb")
FUNC = Unique("@func")
IF = Unique("@if")
COST = Unique("@cost")

BASE = {}
BASE[Symbol("+")] = op.add
BASE[Symbol("-")] = op.sub
BASE[Symbol("*")] = op.mul
BASE[Symbol("/")] = op.div
BASE[Symbol("print")] = lambda x: L(x) and x

CONSTS = {
	"@true"		: True,
	"@false"	: False,
	"@none"		: None,
	"@app"		: APP,
	"@let"		: LET,
	"@lamb"		: LAMB,
	"@func"		: FUNC,
	"@if"		: IF,
	"@cost"		: COST,
}

def isFn(x): return hasattr(x, '__call__')

INF = float('inf')

class Cost(namedtuple('Cost', ['eval', 'app'])): pass
COST_1 = Cost(1, INF)
COST_1_1 = Cost(1, COST_1)


CBASE = {}
CBASE[Symbol("+")] = COST_1_1
CBASE[Symbol("-")] = COST_1_1
CBASE[Symbol("*")] = COST_1_1
CBASE[Symbol("/")] = COST_1_1
CBASE[Symbol("print")] = COST_1











