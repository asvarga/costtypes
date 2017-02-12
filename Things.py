
from collections import namedtuple
from Disp import *
import operator as op

####    ####    ####    ####    ####    ####    ####    ####    

class Expr(tuple):
	def __init__(self, *args): 
		self.type = None
		tuple.__init__(self, *args)
	def __repr__(self): 
		end = ":"+repr(self.type) if self.type else ""
		if self[0] == APP: return "("+" ".join(map(repr, self[1:]))+")"+end
		else: return "["+" ".join(map(repr, self))+"]"+end
class Symbol(str):
	def __repr__(self): return self
class Unique(): 
	def __init__(self, name): self.name = name
	def __repr__(self): return self.name
class Closure(namedtuple('Closure', ['args', 'body', 'nv', 'type'])):
	def __repr__(self): 
		return "[@lamb "+" ".join(map(repr, self.args))+" "+repr(self.body)+"]:"+repr(self.type)
class Function(namedtuple('Function', ['name', 'args', 'body', 'nv', 'type'])):
	def __repr__(self): 
		return "[@func "+self.name+" "+" ".join(map(repr, self.args))+" "+repr(self.body)+"]:"+repr(self.type)
class Env(object):
	def __init__(self, d, nv): self.d, self.nv = d, nv
	def __getitem__(self, key):
		return self.d[key] if key in self.d else self.nv[key]

APP = Unique("@app")
APPQ = Unique("@app?")
LET = Unique("@let")
LAMB = Unique("@lamb")
FUNC = Unique("@func")
IF = Unique("@if")
COST = Unique("@cost")

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

class Pair():
	def __init__(self, car, cdr): self.car, self.cdr = car, cdr
	def __repr__(self): 
		if self is INFPAIR: return "."
		return "("+repr(self.car)+" "+repr(self.cdr)+")"
INFPAIR = Pair(INF, None)
INFPAIR.cdr = INFPAIR
def cons(car, cdr):
	if (car, cdr) == (INF, INFPAIR): return INFPAIR
	return Pair(car, cdr)

VTYPE = cons(1, INFPAIR)
OPTYPE = cons(1, VTYPE)

def tMax(t1, t2):
	if t1 == INFPAIR or t2 == INFPAIR: return INFPAIR
	return cons(max(t1.car, t2.car), tMax(t1.cdr, t2.cdr))
def tAdd(t, x): return cons(t.car+x, t.cdr)
def tRed(t): return Pair(1, t.cdr)

# print VTYPE.cRed, VTYPE.tRes
# ft = FType(10, VTYPE)
# print ft.cRed, ft.tRes, ft.cApp, ft.tRet
# et = EType(100, ft)
# print et.cRed, et.tRes, et.tRes.cApp

BASE = {}
BASE[Symbol("+")] = op.add
BASE[Symbol("-")] = op.sub
BASE[Symbol("*")] = op.mul
BASE[Symbol("/")] = op.div
BASE[Symbol("sqr")] = lambda x: x*x
BASE[Symbol("x")] = 3
BASE[Symbol("y")] = 4
BASE[Symbol("print")] = lambda x: L(x) and x


CBASE = {}
CBASE[Symbol("+")] = OPTYPE
CBASE[Symbol("-")] = OPTYPE
CBASE[Symbol("*")] = OPTYPE
CBASE[Symbol("/")] = OPTYPE
CBASE[Symbol("sqr")] = OPTYPE
CBASE[Symbol("x")] = VTYPE
CBASE[Symbol("y")] = VTYPE











