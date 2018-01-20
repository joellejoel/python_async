import asyncio



loop = asyncio.get_event_loop()
future1 = asyncio.Future()
future2 = asyncio.Future()

def my_coro(future, name, sleep):
	print(name + " is in my coro")
	yield from asyncio.sleep(sleep)
	future.set_result('{0} is done'.format(name))


def my_result(future):
	print(future.result())

tasks = [
	my_coro(future1, 'task1', 10),
	my_coro(future2, 'task2', 5),]

future1.add_done_callback(my_result)
future2.add_done_callback(my_result)

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

