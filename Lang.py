
from Parsing import *
from Disp import *

####    ####    ####    ####    ####    ####    ####    ####    

VERBOSE = False
def VL(*args): return L(*args) if VERBOSE else L

def runf(file_name):
	with open(file_name, 'r') as f: runs(f.read())
def runs(x, nv=None, tnv=None): 
	typ, new, result = None, None, None
	with L("TYPING..."): typ, new = getType(parse(x), tnv or Env({}, CBASE))
	with L("RESULTS:"):
		L("type:", typ)
		with L("modified:"): L(new)
	with L("RUNNING..."): result = run(new, nv or Env({}, BASE))
	with L("RESULT:"): L(result)

def run(x, nv, cs=None):
	cs = cs or INFPAIR

	def app(f, *args):
		if isFn(f): return f(*args)
		if isinstance(f, Closure):
			nv2 = Env(dict(zip(f.args, args)), f.nv)
			return run(f.body, nv2, cs)
		if isinstance(f, Function):
			nv2 = Env(dict(zip(f.args, args)+[(f.name, f)]), f.nv)
			return run(f.body, nv2, cs)

	if isinstance(x, Expr):
		first, rest = x[0], x[1:]
		if first is APP or first is APPQ:
			f = run(rest[0], nv, cs)
			if first is APPQ: 
				cs = pAdd(cs, -f.type.car)
				with VL("@app?:", f): VL("credStack:", cs)
				if cs.car < 0: raise CreditException	
			return app(f, *[run(r, nv, cs) for r in rest[1:]])
		if first is LRUN:
			limit, body, fail = rest
			newCS = cons(limit-body.type.car-fail.type.car, cs)
			try: return run(body, nv, newCS)
			except CreditException, e: 
				with VL("caught:"): VL(repr(e))
				# return run(fail, nv, cs)
				try: return run(fail, nv, cons(0, cs))
				except CreditException, e: return None
		if first is FRUN:
			body, fail = rest
			newCS = cons(cs.car-body.type.car-fail.type.car, cs)
			try: 
				if newCS.car < 0: raise CreditException
				return run(body, nv, newCS)
			except CreditException, e: 
				with VL("caught:"): VL(repr(e))
				return run(fail, nv, cs)

		if first is DRUN:
			limit, body, fail = rest
			limit = min(app(run(limit, nv, cs), cs.car), cs.car)
			newCS = cons(limit, cs)
			try: 
				if newCS.car < 0: raise CreditException
				return run(body, nv, newCS)
			except CreditException, e: 
				with VL("caught:"): VL(repr(e))
				return run(fail, nv, cs)

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
		if first is IF:
			return run(rest[1], nv, cs) if run(rest[0], nv, cs) else run(rest[2], nv, cs)
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
		elif first is LRUN:
			limit = rest[0]
			tBody, newBody = getType(rest[1], nv)
			tFail, newFail = getType(rest[2] or APPNOOP, nv)
			if tBody.car > limit: xType, xNew = tFail, newFail
			else:
				newBody.type = tBody
				newFail.type = tFail
				xType = cons(limit, pMax(tBody.cdr, tFail.cdr))
				xNew = Expr([first, limit, newBody, newFail])
		elif first is FRUN:
			tBody, newBody = getType(rest[0], nv)
			tFail, newFail = getType(rest[1] or APPNOOP, nv)
			newBody.type = tBody
			newFail.type = tFail
			xType = cons(3, pMax(tBody.cdr, tFail.cdr))
			xNew = Expr([first, newBody, newFail])

		elif first is DRUN:
			tLimit, newLimit = getType(rest[0], nv)
			tBody, newBody = getType(rest[1], nv)
			tFail, newFail = getType(rest[2], nv)
			# newLimit.type = tLimit
			# newBody.type = tBody
			# newFail.type = tFail
			xType_car = tLimit.car+tLimit.cdr.car+tBody.car+tFail.car+3
			xType = cons(xType_car, pMax(tBody.cdr, tFail.cdr))
			xNew = Expr([first, newLimit, newBody, newFail])

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
			xNew.type = xType.cdr
		elif first is IF:
			types, new = zip(*[getType(r, nv) for r in rest])
			xType = pAdd(pMax(types[1], types[2]), types[0].car)
			xNew = Expr([first]+list(new))
		elif first is SEQ:
			types, new = zip(*[getType(r, nv) for r in rest])
			xNew = Expr([first]+list(new))
			xType = cons(sum(t.car for t in types), INFPAIR)
		return xType, xNew
	if isinstance(x, Symbol): return nv[x], x
	return VTYPE, x









