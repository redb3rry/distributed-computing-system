import abc
import asyncio
import websockets
import sys

connectionCounter = 0
tasks = []

class Server(abc.ABC):
    @abc.abstractmethod
    def create_tasks(self, data, num_of_workers):
        pass

    @abc.abstractmethod
    def read_data(self, filename):
        pass

    @abc.abstractmethod
    def add_to_results(self, result, connection_number):
        pass

    async def handle_connection(self, websocket, path):
        global connectionCounter
        await websocket.send(str(tasks[connectionCounter]))
        result = await websocket.recv()
        self.add_to_results(result, connectionCounter)
        connectionCounter += 1

    def run(self, address, port, filename):
        global tasks

        num_of_workers = int(sys.argv[1])
        data = self.read_data(filename)
        tasks = self.create_tasks(data, num_of_workers)

        start_server = websockets.serve(self.handle_connection, address, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
