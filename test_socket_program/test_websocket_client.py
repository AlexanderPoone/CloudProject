import asyncio
import websockets
import time

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        f = open("test_data","r")
        data = f.read()
        start_time = time.time()
        await websocket.send(data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("websocket")
        print("elapsed time:"+str(elapsed_time)+" seconds")
        f.close()

asyncio.get_event_loop().run_until_complete(
    hello('ws://ec2-34-203-214-59.compute-1.amazonaws.com:7000'))
