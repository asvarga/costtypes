
from z3 import *
init("/Users/avarga/z3/bin")

from Things import *
from Disp import *

########

SBASE = {}
SBASE[Symbol("+")] = OPTYPE
SBASE[Symbol("-")] = OPTYPE
SBASE[Symbol("*")] = OPTYPE
SBASE[Symbol("/")] = OPTYPE
SBASE[Symbol("sqr")] = OPTYPE
SBASE[Symbol("neg")] = OPTYPE
SBASE[Symbol("x")] = VTYPE
SBASE[Symbol("y")] = VTYPE
SBASE[Symbol("print")] = OPTYPE
SBASE[Symbol("box")] = OPTYPE
SBASE[Symbol("get")] = OPTYPE
SBASE[Symbol("set")] = OPTYPE
SBASE[Symbol("id")] = OPTYPE
SBASE[Symbol("noop")] = OPTYPE
SBASE[Symbol("int")] = OPTYPE

########

def smt(x):
	L(test(x))

def test(x, nv=None, cs=None):
	nv = nv or Env({}, SBASE)

	def app(f, *args):
		if isFn(f): pass
		if isinstance(f, Closure): pass
		if isinstance(f, Function): pass

	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP or first is APPQ: pass

		if first is LRUN: pass
		if first is FRUN: pass
		if first is DRUN: pass

		if first is LET: pass
		if first is LAMB: pass
		if first is FUNC: pass
		if first is IF: pass
		if first is SEQ: pass
	if isinstance(x, Symbol): pass
	return 1







