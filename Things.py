
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

# class Type(): 
# 	cRed, cApp = 1, INF
# 	def __init__(self): self.tRes, self.tRet = self, self
# 	def __repr__(self): return "VTYPE"
# class FType(Type):
# 	def __init__(self, cApp, tRet): 
# 		self.tRes, self.cApp, self.tRet = self, cApp, tRet
# 	def __repr__(self): return "("+str(self.cApp)+"->"+repr(self.tRet)+")"
# class EType(Type):
# 	def __init__(self, cRed, tRes): self.cRed, self.tRes = cRed, tRes
# 	def __repr__(self): return "("+str(self.cRed)+".."+repr(self.tRes)+")"
# VTYPE = Type()
# OPTYPE = FType(1, VTYPE)

SEMI = Unique(';')
class Type():
	def __init__(self, cRed=None, tRed=None, cApp=None, tApp=None):
		self.cRed = cRed or 0
		self.tRed = tRed or self
		self.cApp = cApp or INF
		self.tApp = tApp or self
	def __repr__(self):
		L = []
		if self.cRed or not self.tRed:
			L.append(repr(self.cRed)+".."+("SELF" if self.tRed is self else repr(self.tRed)))
		if self.cApp != INF or not self.tApp is self:
			L.append(repr(self.cApp)+"->"+("SELF" if self.tApp is self else repr(self.tApp)))
		return "("+" | ".join(L)+")"
	def add(self, x):
		return Type(self.cRed+x, self.tRed, self.cApp, self.tApp)

VTYPE = Type()
def EType(cRed, tRed): return Type(cRed, tRed)
def FType(cApp, tApp): return Type(None, None, cApp, tApp)
OPTYPE = FType(1, VTYPE)

# def maxType(t1, t2):
# 	if t1 == t2 == VTYPE: return VTYPE
# 	m_cRed = max(t1.cRed, t2.cRed)
# 	m_tRed = maxType(t1.tRed, t2.tRed)
# 	m_cApp = max(t1.cApp, t2.cApp)
# 	m_tApp = maxType(t1.tApp, t2.tApp)
# 	return Type(m_cRed, m_tRed, m_cApp, m_tApp)


# VTYPE = [1]
# OPTYPE = [1, 1]
# def tMax(t1, t2):
# 	L = min(len(t1), len(t2))
# 	return map(max, zip(t1, t2))+t1[L:]+t2[L:]
# def tAdd(t, x): return [t[0]+x]+t[1:]


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
BASE[Symbol("x")] = 3
BASE[Symbol("y")] = 4
BASE[Symbol("print")] = lambda x: L(x) and x

CBASE = {}
CBASE[Symbol("+")] = OPTYPE
CBASE[Symbol("-")] = OPTYPE
CBASE[Symbol("*")] = OPTYPE
CBASE[Symbol("/")] = OPTYPE
CBASE[Symbol("x")] = VTYPE
CBASE[Symbol("y")] = VTYPE











