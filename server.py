import socket
from threading import *

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

clients = []


def listener(conn_m, addr_m):
    print("Регистрация нового клиента")
    while True:
        msg = ''
        data = conn_m.recv(1024)
        msg += data.decode()
        conn_m.send("Вы написали: ".encode() + data)
        for client_each in clients:
            if client_each != conn_m:
                client_each.send(str(addr_m[0]).encode() + ": ".encode() + data)
        print(addr_m[0] + ": " + msg)


print("Сервер запущен")
while True:
    conn, addr = sock.accept()
    msg = ''
    data = conn.recv(1024)
    msg += data.decode()
    if msg != 'scanner_command':
        clients.append(conn)
        client = Thread(target=listener, args=(conn, addr))
        client.run()
    else:
        continue
