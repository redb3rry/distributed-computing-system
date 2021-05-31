import asyncio
import websockets
import abc


class Worker(abc.ABC):
    @abc.abstractmethod
    def do_work(self, task):
        return 0

    def __init__(self, uri):
        self.uri = uri

    async def handle_connection(self):
        async with websockets.connect(self.uri) as websocket:
            task = await websocket.recv()
            result = self.do_work(task)
            await websocket.send(result)

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.handle_connection())
