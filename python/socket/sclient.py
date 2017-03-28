import socket

HOST=""
PORT=50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = raw_input("your msg::").strip()
    if len(msg) == 0: continue
    s.sendall(msg)
    data=s.recv(1024)
    print "received:",data

s.close()

