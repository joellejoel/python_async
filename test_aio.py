import aiohttp
import asyncio
import async_timeout

@asyncio.coroutine
def fetch(session, url):
	with aiohttp.Timeout(10):
		resp = yield from session.get(url)
		try:
			return (yield from resp.text())
		except:
			yield from resp.release()
		#with (yield from session.get(url)) as response:
		#	return (yield from response.text())

@asyncio.coroutine
def main():
	with (aiohttp.ClientSession()) as session:
		html = yield from fetch(session, 'http://python.org')
		print(html)




loop = asyncio.get_event_loop()
loop.run_until_complete(main())

