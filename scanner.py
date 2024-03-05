import asyncio

class Connect(asyncio.Transport):
    def connection_made(self, transport):
        transport.close()
    def connection_lost(self, exc):
        pass


async def connection(ip, port):
    loop = asyncio.get_running_loop()
    await asyncio.wait_for(loop.create_connection(Connect, ip, port), 0.05)
    return port


async def main():
    ip = '127.0.0.1'
    portrange = (3389, 3390)
    loop = asyncio.get_running_loop()
    routines = []

    def callback(routine):
        routines.remove(routine)
        print(routine.result())

    for port in range (*portrange):
        routines.append(loop.create_task(connection(ip, port)))
        routines[-1].add_done_callback(callback)

    while len(routines) > 0:
        await asyncio.sleep(1)

asyncio.run(main())