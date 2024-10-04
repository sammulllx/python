import socket

server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_s.bind(("", 7892))

server_s.listen(128)

new_s, client_info = server_s.accept()

print(client_info)


while True:
    recv_cotent = new_s.recv(1024)
    if len(recv_cotent) != 0:
        print(recv_cotent.decode("utf-8"))
    else:
        new_s.close()
        break
