
from Parsing import *
from Disp import *

####    ####    ####    ####    ####    ####    ####    ####    

def runf(file_name):
	with open(file_name, 'r') as f: L(runs(f.read()))
def runs(x, nv=None): return run(parse(x), nv or Env({}, BASE))
def run(x, nv):
	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP:
			rest = [run(r, nv) for r in rest]
			f, args = rest[0], rest[1:]
			if isFn(f): return f(*args)
			nv2 = Env(dict(zip(f.args, args)), f.nv)
			return run(f.body, nv2)
		if first is LET:
			arg, val, body = rest
			nv2 = Env({arg: run(val, nv)}, nv)
			return run(body, nv2)
		if first is LAMB:
			args, body = rest[:-1], rest[-1]
			return Closure(args, body, nv)
		if first is COST:
			return minCost(rest[0], nv)
	if isinstance(x, Symbol): return nv[x]
	return x

def minCost(x, nv):
	return INF


# def run(x, nv):
# 	if isinstance(x, Pair): 
# 		L, R = run(x.L, nv), run(x.R, nv)
# 		if isinstance(L, Lambda): 
# 			nv2 = Env(dict(zip(L.args.val, R)), L.nv, nv)
# 			return run(L.body.val, nv2)
# 		return L(*R)
# 	if isinstance(x, Rail): return Array([run(xi, nv) for xi in x])
# 	if isinstance(x, Symbol): return eget(nv, x)
# 	if x is NV:		return nv
# 	if x is SNV: 	return nv.snv
# 	if x is DNV: 	return nv.dnv
# 	if x is RUN: 	return runq
# 	return x
