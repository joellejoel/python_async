import asyncio


@asyncio.coroutine
def my_coro(name, sleep):
	print('{0} gonna sleep for: {1} seconds'.format(name,sleep))
	
	yield from asyncio.sleep(sleep)
	print('{0} is woke now '.format(name))


loop = asyncio.get_event_loop()

tasks = [
	my_coro('task1', 10),
	my_coro('task2', 5),
	my_coro('task3', 1),
	]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()




if __name__ == "__main__":
	print("hello")
