import socket
import threading
from Parser import Parser
class Backend:
    def __init__(self):
        self.routes = {}

    def run(self,port=3000):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(("127.0.0.1",port))
        sock.listen(1)
        while True:
            con , add = sock.accept()

            data = b""
            while True:
                got = con.recv(1024)
                data += got
                if got == b"":
                    break
                if got[-4:] == b"--\r\n":
                    break
                if b"x-www-form-urlencoded" in data and b"\r\n\r\n" in data:
                    break
                if (b"Content-Length" not in data) and (data and (data[-4:] == b"\r\n\r\n")):
                    break
            Parser.ParserRequestFactory(data)
            con.send(b"""HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: my_cookie=example_value; Expires=Wed, 06 Aug 2023 23:59:59 GMT; Path=/
Content-Length: 30

<html><body>Hello, World!</body></html>
""")
            con.close()

if __name__ == "__main__":
    backend = Backend()
    backend.run(1000)
