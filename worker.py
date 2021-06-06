import ast
import asyncio

import websockets


class Worker:

    def __init__(self, uri, do_work):
        self.uri = uri
        self.do_work = do_work

    async def handle_connection(self):
        async with websockets.connect(self.uri, max_size=300000000) as websocket:
            task = await websocket.recv()
            task = ast.literal_eval(task)
            result = self.do_work(task)
            await websocket.send(str(result))

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.handle_connection())
