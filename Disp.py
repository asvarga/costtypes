
# a cool logger
class Logger(object):
	def __init__(self): self.indent = 0
	def __call__(self, x): 
		indent = "\t"*self.indent
		print indent+indent.join(str(x).splitlines(True))
		return self
	def __enter__(self): self.indent += 1
	def __exit__(self, type, value, traceback): self.indent -= 1

L = Logger()

# # example
# with L("aaa:"):
# 	with L("bbb:"):
# 		L("ccc")

