import asyncio
import websockets
from dynamicqrauth import tokengen, createbase64QR

async def sendqr(websocket, path):
    url = "https://attandance-app.herokuapp.com/getattendance"
    token = tokengen(url)
    qr = createbase64QR(url, token)

    qr_request = await websocket.recv()
    print(qr_request)
    await websocket.send(qr)

start_server = websockets.serve(sendqr, '0.0.0.0', 80)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

    # name = await websocket.recv()
    # print(f"< {name}")

    # greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    # print(b"> {greeting}")