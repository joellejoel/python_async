""" 
	yield statement examples:
		yield (expr)
		yield from (expr)
	yield expression examples:
		(yield expr)
		(yield from expr)
"""
"""
	this is pretty fun, control flow is from:
		a. first()
		b. writer_wrapper() <-> writer()
"""

def writer():
	"""A coroutine that writes data *sent* to it to fd, socket, etc
		using yield from"""
	while True:
		w = (yield)	
		print('>>', w)

def writer_wrapper(coro):
	coro.send(None)
	while True:
		try:
			x = (yield)
			coro.send(x)
		except StopIteration:
			pass


def first():	
	w = writer()
	wrap = writer_wrapper(w)
	wrap.send(None) # prime the coro
	for i in range(4):
		wrap.send(i)
	


if __name__ == "__main__":
	first()
