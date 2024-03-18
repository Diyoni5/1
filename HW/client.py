import asyncio
import pickle

from common import AAA, A
from penguin import *

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print(f'{self.message}')

    def datagram_received(self, data):
        birds = pickle.loads(data)
        birds.swim()

    def connection_lost(self, exc):
        print("Bye-Bye :(")
        self.on_con_lost.set_result(True)

async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    message = "Hiiiii! I'm starting."

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        AAA, A)

    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())


