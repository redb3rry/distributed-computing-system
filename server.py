import asyncio
import sys

import websockets


class Server:
    connectionCounter = 0
    finishedCounter = 0
    num_of_workers = 0
    tasks = []
    results = []

    def __init__(self, create_tasks, read_data, add_to_results):
        self.create_tasks = create_tasks
        self.read_data = read_data
        self.add_to_results = add_to_results

    async def handle_connection(self, websocket, path):
        my_count = self.connectionCounter
        self.connectionCounter += 1
        await websocket.send(str(self.tasks[my_count]))
        result = await websocket.recv()
        self.results = self.add_to_results(result, my_count, self.results, self.num_of_workers)
        self.finishedCounter += 1
        print("Worker #" + str(my_count) + " has finished working")
        if self.finishedCounter == self.num_of_workers:
            print(self.results)

    def run(self, address, port, filename):
        if len(sys.argv) < 2:
            exit("You need to pass number of workers as an argument.")
        self.num_of_workers = int(sys.argv[1])
        data = self.read_data(filename)
        result_rows = len(data[0])
        result_cols = len(data[0][0])
        if not self.results:
            self.results = [[0 for i in range(result_cols)] for j in range(result_rows)]
        self.tasks = self.create_tasks(data, self.num_of_workers)

        start_server = websockets.serve(self.handle_connection, address, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
