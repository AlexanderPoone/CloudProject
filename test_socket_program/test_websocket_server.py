import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message,'received from client')

print("start listen")
asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 7000))
asyncio.get_event_loop().run_forever()
