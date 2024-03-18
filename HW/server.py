import asyncio
import pickle

from random import randint

from common import AAA, A
from penguin import *

def use():
    r = randint(0, 20)
    if r % 2 == 0:
        bird = Penguin('Emperor Penguin', '130', '25', '35', '40')
    else:
        bird = Penguin('Rockhopper Penguin', '60', '25', '2', '3')
    return bird

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def datagram_received(self, data):
        message = data.decode()
        print('Received: {}'.format(message))

        birds = use()
        answ = pickle.dumps(birds)
        print('Send:')
        self.transport.write(answ)

        print('I`m closing?')
        self.transport.close()

async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        AAA, A)

    async with server:
        await server.serve_forever()


asyncio.run(main())






