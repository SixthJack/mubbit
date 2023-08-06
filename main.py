from Mubbit import mubbit
import socket
import threading
import sys
import os
sys.path.append(os.getcwd())


def SpawnerOfSpawner(routes, middlewares):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 1000))
    sock.listen(1)
    while True:
        try:
            con, add = sock.accept()
            threading.Thread(target=Spawner, args=(
                con, routes, middlewares)).start()
        except Exception as e:
            print("An exception occured")


def Spawner(con, routes, middlewares):
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
    data = mubbit.mubbit(routes, middlewares, data).encode()
    con.send(data)
    con.close()


class Backend:
    def __init__(self):
        self.routes = {}
        self.middlewares = []

    def run(self, port=3000):
        thread = threading.Thread(
            target=SpawnerOfSpawner, args=(self.routes, self.middlewares))
        thread.start()
        thread.join()


if __name__ == "__main__":
    backend = Backend()
    backend.run()
