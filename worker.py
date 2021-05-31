import asyncio
import websockets


def do_work(task):
    return 0


async def handle_connection():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        task = await websocket.recv()
        result = do_work(task)
        await websocket.send(result)


def run():
    asyncio.get_event_loop().run_until_complete(handle_connection())
