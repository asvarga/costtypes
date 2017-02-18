
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
	def __getitem__(self, ind):
		return tuple.__getitem__(self, ind) if ind < len(self) else None
	def __getslice__(self, i, j):
		return Expr(tuple.__getslice__(self, i, j))
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
class Op():
	def __init__(self, op, typ, name="some_op"): 
		self.op , self.type, self.name = op, typ, name
	def __call__(self, *args, **kwargs): return self.op(*args, **kwargs)
	def __repr__(self): return self.name
class Box():
	def __init__(self, val): self.val = val
	def setVal(self, val): self.val = val
	def __repr__(self): return "(box "+repr(self.val)+")"


class CreditException(Exception): pass
# class TypeException(Exception): pass

APP = Unique("@app")
APPQ = Unique("@app?")
LET = Unique("@let")
LAMB = Unique("@lamb")
FUNC = Unique("@func")
IF = Unique("@if")
LRUN = Unique("@lrun")
FRUN = Unique("@frun")
DRUN = Unique("@drun")
TRY = Unique("@try")
# RAISE = Unique("@raise")
COST = Unique("@cost")
SEQ = Unique("@seq")

CONSTS = {
	"@true"		: True,
	"@false"	: False,
	"@none"		: None,
	"@app"		: APP,
	"@let"		: LET,
	"@lamb"		: LAMB,
	"@func"		: FUNC,
	"@if"		: IF,
	"@lrun"		: LRUN,
	"@frun"		: FRUN,
	"@drun"		: DRUN,
	"@try"		: TRY,
	# "@raise"	: RAISE,
	"@cost"		: COST,
	"@seq"		: SEQ,
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

def pMax(t1, t2):
	if t1 == INFPAIR or t2 == INFPAIR: return INFPAIR
	return cons(max(t1.car, t2.car), pMax(t1.cdr, t2.cdr))
def pAdd(t, x): return cons(t.car+x, t.cdr)
def pRed(t): return Pair(1, t.cdr)

NOOP = Op(lambda *args: None, OPTYPE, "noop")
APPNOOP = Expr([APP, NOOP])

BASE = {}
BASE[Symbol("+")] = Op(op.add, OPTYPE, "+")
BASE[Symbol("-")] = Op(op.sub, OPTYPE, "-")
BASE[Symbol("*")] = Op(op.mul, OPTYPE, "*")
BASE[Symbol("/")] = Op(op.div, OPTYPE, "/")
BASE[Symbol("sqr")] = Op(lambda x: x*x, OPTYPE, "sqr")
BASE[Symbol("neg")] = Op(lambda x: -x, OPTYPE, "neg")
BASE[Symbol("x")] = 3
BASE[Symbol("y")] = 4
BASE[Symbol("print")] = Op(L.log, OPTYPE, "print")
BASE[Symbol("box")] = Op(lambda val: Box(val), OPTYPE, "box")
BASE[Symbol("get")] = Op(lambda box: box.val, OPTYPE, "get")
BASE[Symbol("set")] = Op(lambda box, val: box.setVal(val), OPTYPE, "set")
BASE[Symbol("id")] = Op(lambda x: x, OPTYPE, "id")
BASE[Symbol("noop")] = NOOP


CBASE = {}
CBASE[Symbol("+")] = OPTYPE
CBASE[Symbol("-")] = OPTYPE
CBASE[Symbol("*")] = OPTYPE
CBASE[Symbol("/")] = OPTYPE
CBASE[Symbol("sqr")] = OPTYPE
CBASE[Symbol("neg")] = OPTYPE
CBASE[Symbol("x")] = VTYPE
CBASE[Symbol("y")] = VTYPE
CBASE[Symbol("print")] = OPTYPE
CBASE[Symbol("box")] = OPTYPE
CBASE[Symbol("get")] = OPTYPE
CBASE[Symbol("set")] = OPTYPE
CBASE[Symbol("id")] = OPTYPE
CBASE[Symbol("noop")] = OPTYPE





