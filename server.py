import abc
import asyncio
import websockets
import sys


class Server(abc.ABC):
    connectionCounter = 0
    finishedCounter = 0
    num_of_workers = 0
    tasks = []
    results = []

    @abc.abstractmethod
    def create_tasks(self, data, num_of_workers):
        pass

    @abc.abstractmethod
    def read_data(self, filename):
        pass

    @abc.abstractmethod
    def add_to_results(self, result, connection_number, results):
        pass

    async def handle_connection(self, websocket, path):
        my_count = self.connectionCounter
        self.connectionCounter += 1
        await websocket.send(str(self.tasks[my_count]))
        result = await websocket.recv()
        self.results = self.add_to_results(result, my_count, self.results)
        self.finishedCounter += 1
        print("Worker #" + str(my_count) + " has finished working")
        if self.finishedCounter == self.num_of_workers:
            print(self.results)

    def run(self, address, port, filename):
        self.num_of_workers = int(sys.argv[1])
        data = self.read_data(filename)
        self.tasks = self.create_tasks(data, self.num_of_workers)

        start_server = websockets.serve(self.handle_connection, address, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
