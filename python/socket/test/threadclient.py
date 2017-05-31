import socket

HOST=""
PORT=50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
with open("msg.txt","r") as f:
    for _line in f.readlines():
        
        while True:
            msg = raw_input("your msg::").strip()
        if len(msg) == 0: continue
        s.sendall(msg)
        data=s.recv(1024)
        print "received:",data

s.close()

