
from Parsing import *
from Disp import *

####    ####    ####    ####    ####    ####    ####    ####    

def runf(file_name):
	with open(file_name, 'r') as f: runs(f.read())
def runs(x, nv=None, tnv=None): 
	typ, new = getType(parse(x), Env({}, CBASE))
	L(typ)
	L(new)
	L(run(new, Env({}, BASE)))
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
		first, rest, xType, xNew = x[0], x[1:], None, x
		if first is APP:
			types, new = zip(*[getType(r, nv) for r in rest])
			f = types[0]
			xType = cons(sum(r.car for r in types)+f.cdr.car, f.cdr.cdr)
			xNew = Expr([first]+list(new))
		elif first is LET:
			arg, val, body = rest
			tVal, newVal = getType(val, nv)
			nv2 = Env({arg: tRed(tVal)}, nv)
			tBody, newBody = getType(body, nv2)
			xType = tAdd(tBody, tVal.car+1)
			xNew = Expr([first, arg, newVal, newBody])
		elif first is LAMB or first is FUNC:
			args = rest[:-1]
			nv2 = Env({arg:VTYPE for arg in args}, nv)
			tBody, newBody = getType(rest[-1], nv2)
			xType = cons(len(rest), tBody)
			xNew = Expr([first]+list(args)+[newBody])
		elif first is IF:
			types, new = zip(*[getType(r, nv) for r in rest])
			xType = tAdd(tMax(types[1], types[2]), types[0].car)
			xNew = Expr([first]+list(new))
		return xType, xNew		# modify here
	if isinstance(x, Symbol): return nv[x], x
	return VTYPE, x

def getType2(x, nv):
	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP:
			rest = [getType(r, nv) for r in rest]
			fRed = rest[0].tRed
			return EType(sum(r.cRed+1 for r in rest)+fRed.cApp, fRed.tApp)
		if first is LAMB:
			args = rest[:-1]
			nv2 = Env({arg:VTYPE for arg in args}, nv)
			body = getType(rest[-1], nv2)
			return EType(len(rest), FType(len(args)+body.cRed, body.tRed))
		if first is IF:
			rest = [getType(r, nv) for r in rest]
			return maxType(rest[1], rest[2]).add(rest[0].cRed)
		raise Exception("unimplemented")
	if isinstance(x, Symbol): return nv[x]	#EType(1, nv[x])
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
