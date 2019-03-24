import asyncio
import websockets
from PIL import Image
import base64
import io
import time

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    image.show()
    # print(type(image))
    # return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


async def receiveqr():
    num = int(input("Number of pings: "))
    while num != 0:
        async with websockets.connect('ws://localhost:8765') as websocket:
            print(num)
            await websocket.send(str(num))
            print('Request Number: '+ str(num))
            qr = await websocket.recv()
            decoded_qr = stringToRGB(qr)
            # cv2.imshow(decoded_qr)
            num -= 1
            time.sleep(3)

asyncio.get_event_loop().run_until_complete(receiveqr())