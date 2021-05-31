import abc
import asyncio
import websockets

connectionCounter = 0
tasks = []


class Server(abc.ABC):
    @abc.abstractmethod
    def create_tasks(self):
        pass

    def read_data(self, filename):
        return 0

    async def handle_connection(self, websocket, path):
        global connectionCounter

        await websocket.send()
        result = await websocket.recv()
        connectionCounter += 1

    def run(self, address, port, filename):
        self.read_data(filename)
        self.create_tasks()

        start_server = websockets.serve(self.handle_connection, address, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
