import socket
import logging
import json
import random
import datetime


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #datagram
s.bind(('0.0.0.0', 10000))
while True:
    message, (ip, port) = s.recvfrom(500)
    logger.info(f"(ip): {message.decode()}")
# print(s.recvfrom(500))


# while True:
#     try:
#         client_socket = s.accept()
#     except TimeoutError:
#         continue
#     client, (addr, port) = client_socket
#     logger.warning(f"{addr} connected from port {port}")


#     data = {
#         "time": datetime.datetime.now().isoformat(),
#         "number": random.random()
#         }
#     client.send(json.dumps(data))
#     # b''.decode()
#     # "".encode()
#     client.close()