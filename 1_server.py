import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = s.bind(('127.0.0.1', 8080))
s.listen(5)
s.setblocking(False)
s.settimeout(5)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    incoming = client.recv(500)
    # print(incoming)
    content = ''
    client.send(content)
    
    client.close()