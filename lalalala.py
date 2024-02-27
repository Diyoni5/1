import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.sendto(b"solodca0", ('192.168.202.99', 10000))
while True:
    text = input()
    s.sendto(text.encode(), ('192.168.202.255', 10000))
