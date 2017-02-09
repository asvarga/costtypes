
from Parsing import *
from Disp import *

####    ####    ####    ####    ####    ####    ####    ####    

def runf(file_name):
	with open(file_name, 'r') as f: L(runs(f.read()))
def runs(x, nv=None): 
	# return run(parse(x), nv or Env({}, BASE))
	return getType(parse(x), nv or Env({}, CBASE))
def run(x, nv):
	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP:
			rest = [run(r, nv) for r in rest]
			f, args = rest[0], rest[1:]
			if isFn(f): return f(*args)
			if isinstance(f, Closure):
				nv2 = Env(dict(zip(f.args, args)), f.nv)
				return run(f.body, nv2)
			if isinstance(f, Function):
				nv2 = Env(dict(zip(f.args, args)+[(f.name, f)]), f.nv)
				return run(f.body, nv2)
		if first is LET:
			arg, val, body = rest
			nv2 = Env({arg: run(val, nv)}, nv)
			return run(body, nv2)
		if first is LAMB:
			args, body = rest[:-1], rest[-1]
			return Closure(args, body, nv)
		if first is FUNC:
			name, args, body = rest[0], rest[1:-1], rest[-1]
			return Function(name, args, body, nv)
		if first is IF:
			return run(rest[1], nv) if run(rest[0], nv) else run(rest[2], nv)
	if isinstance(x, Symbol): return nv[x]
	return x

def getType(x, nv):
	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP:
			rest = [getType(r, nv) for r in rest]
			fRes = rest[0].tRes
			return EType(sum(r.cRed+1 for r in rest)+fRes.cApp, fRes.tRet)
		# if first is IF:
		# 	maxCost = max(getType(rest[1], nv).eval, getType(rest[2], nv).eval)
		# 	return Cost(1+getType(rest[0], nv).eval+maxCost, INF)
		raise Exception("unimplemented")
	if isinstance(x, Symbol): return EType(1, nv[x])
	return VTYPE


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
