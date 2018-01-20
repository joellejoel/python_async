

def fake_text_file():
	yield 1
	yield 2
	yield 3

def test_wrapper(g):
	yield from g

print(fake_text_file())

wrap = test_wrapper(fake_text_file())
for x in wrap:
	print(x)


for x in fake_text_file():
	print(str(x+3))
