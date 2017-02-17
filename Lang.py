
from Parsing import *
from Disp import *

####    ####    ####    ####    ####    ####    ####    ####    

def runf(file_name):
	with open(file_name, 'r') as f: runs(f.read())
def runs(x, nv=None, tnv=None): 
	# L(run(parse(x), nv or Env({}, BASE)))
	typ, new, result = None, None, None
	with L("TYPING..."):
		typ, new = getType(parse(x), tnv or Env({}, CBASE))
	with L("RESULTS:"):
		with L("type:"): L(typ)
		with L("modified:"): L(new)
	with L("RUNNING..."):
		result = run(new, nv or Env({}, BASE))
	with L("RESULT:"):
		L(result)

def run(x, nv, cs=None):
	cs = cs or INFPAIR
	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP or first is APPQ:
			f = run(rest[0], nv, cs)
			if first is APPQ: 
				cs = pAdd(cs, -f.type.car)
				# with L("@app?"): L(f) and L(f.type) and L(cs)
				if cs.car < 0: raise RunException	
			args = [run(r, nv, cs) for r in rest[1:]]
			if isFn(f): return f(*args)
			if isinstance(f, Closure):
				nv2 = Env(dict(zip(f.args, args)), f.nv)
				return run(f.body, nv2, cs)
			if isinstance(f, Function):
				nv2 = Env(dict(zip(f.args, args)+[(f.name, f)]), f.nv)
				return run(f.body, nv2, cs)
		if first is LET:
			arg, val, body = rest
			nv2 = Env({arg: run(val, nv, cs)}, nv)
			return run(body, nv2, cs)
		if first is LAMB:
			args, body = rest[:-1], rest[-1]
			return Closure(args, body, nv, x.type)
		if first is FUNC:
			name, args, body = rest[0], rest[1:-1], rest[-1]
			return Function(name, args, body, nv, x.type)
		if first is LRUN:
			limit, body = rest
			newCS = cons(limit, cs)
			return run(body, nv, newCS)
		if first is IF:
			return run(rest[1], nv, cs) if run(rest[0], nv, cs) else run(rest[2], nv, cs)
		if first is TRY:
			body, fail = rest
			try: return run(body, nv, cs)
			except RunException, e: 
				# with L("caught:"): L(repr(e))
				return run(fail, nv, cs)
		# if first is RAISE:
		# 	raise RunException
		if first is SEQ:
			for r in rest: run(r, nv, cs)
			return None
	if isinstance(x, Symbol): return nv[x]
	return x

def getType(x, nv):
	if isinstance(x, Expr):
		first, rest, xType, xNew = x[0], x[1:], None, x
		if first is APP:
			types, new = zip(*[getType(r, nv) for r in rest])
			fType, argTypes = types[0], types[1:]
			if fType.cdr is INFPAIR: 
				xNew = Expr([APPQ]+list(new))
				xType = cons(sum(r.car for r in types), INFPAIR)
			else:
				xNew = Expr([APP]+list(new))
				xType = pAdd(fType.cdr, sum(r.car for r in types))
		elif first is LET:
			arg, val, body = rest
			tVal, newVal = getType(val, nv)
			nv2 = Env({arg: pRed(tVal)}, nv)
			tBody, newBody = getType(body, nv2)
			xType = pAdd(tBody, tVal.car+1)
			xNew = Expr([first, arg, newVal, newBody])
		elif first is LAMB or first is FUNC:
			args = rest[:-1]
			nv2 = Env({arg:VTYPE for arg in args}, nv)
			tBody, newBody = getType(rest[-1], nv2)
			xType = cons(len(rest), tBody)
			xNew = Expr([first]+list(args)+[newBody])
			xNew.type = xType
		elif first is IF:
			types, new = zip(*[getType(r, nv) for r in rest])
			xType = pAdd(pMax(types[1], types[2]), types[0].car)
			xNew = Expr([first]+list(new))
		if first is LRUN:
			limit = rest[0]
			tBody, newBody = getType(rest[1], nv)
			if tBody.car > limit: raise TypeException
			xNew = Expr([first, limit-tBody.car, newBody])
			xType = cons(limit+1, tBody.cdr)
		if first is TRY:
			tBody, newBody = getType(rest[0], nv)
			tFail, newFail = getType(rest[1], nv)
			xNew = Expr([first, newBody, newFail])
			xType = cons(tBody.car+tFail.car, pMax(tBody.cdr, tFail.cdr))
		if first is SEQ:
			types, new = zip(*[getType(r, nv) for r in rest])
			xNew = Expr([first]+list(new))
			xType = cons(sum(t.car for t in types), INFPAIR)
		return xType, xNew
	if isinstance(x, Symbol): return nv[x], x
	return VTYPE, x









