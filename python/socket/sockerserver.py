
import SocketServer
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handler(self):
        while True:
            data = self.request.recv(1024)
            if not data: break
            print data
            self.request.sendall(data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1",50007
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()

