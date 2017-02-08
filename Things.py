
from collections import namedtuple

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
		return "[lamb@ "+" ".join(map(repr, self.args))+" "+repr(self.body)+"]"
class Env(object):
	def __init__(self, d, nv): self.d, self.nv = d, nv
	def __getitem__(self, key):
		return self.d[key] if key in self.d else self.nv[key]

APP = Unique("@app")
LET = Unique("@let")
LAMB = Unique("@lamb")

BASE = {}
BASE[Symbol("+")] = lambda x,y: x+y
BASE[Symbol("-")] = lambda x,y: x-y
BASE[Symbol("*")] = lambda x,y: x*y
BASE[Symbol("/")] = lambda x,y: x/y

CONSTS = {
	"@true"		: True,
	"@false"	: False,
	"@none"		: None,
	"@app"		: APP,
	"@let"		: LET,
	"@lamb"		: LAMB,
}

def isFn(x): return hasattr(x, '__call__')






