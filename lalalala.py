import socket

from common import AAA

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(AAA)
print(s.recv(500))