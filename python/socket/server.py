
import socket

HOST=""
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

#conn,addr = s.accept()
#print "accept by",addr

while True:
    conn,addr = s.accept()
    print "accept by",addr

    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data.upper())
    
    conn.close()


    

