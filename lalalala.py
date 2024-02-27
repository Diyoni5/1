import socket
import json
from common import AAA

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(AAA)
data = json.loads(s.recv(500).decode())

print(f"got {data}, {type(data)}")
