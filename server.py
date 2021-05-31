import asyncio
import websockets

connectionCounter = 0
tasks = []


def create_tasks():
    return 0


def read_data(filename):
    return 0


async def handle_connection(websocket, path):
    global connectionCounter

    await websocket.send()
    result = await websocket.recv()
    connectionCounter += 1


def run(address, port, filename):
    read_data(filename)
    create_tasks()

    start_server = websockets.serve(handle_connection, address, port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

