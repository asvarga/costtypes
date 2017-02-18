
# a cool logger
class Logger(object):
	def __init__(self): self.indent = 0
	def __call__(self, *args): 
		indent = "\t"*self.indent
		S = " ".join(map(str, args))
		print indent+indent.join(S.splitlines(True))
		return self
	def __enter__(self): self.indent += 1
	def __exit__(self, type, value, traceback): self.indent -= 1
	def log(self, *args):
		self(*args)
		return args[-1]

L = Logger()

# # example
# with L("aaa:"):
# 	with L("bbb:"):
# 		L("ccc")

