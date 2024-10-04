# 可以开多个comtool同时连接TCP服务器

import socket
import threading


class HandleData(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            recv_cotent = self.client_socket.recv(1024)
            if len(recv_cotent) != 0:
                print(recv_cotent.decode("utf-8"))
                self.client_socket.send(recv_cotent)
            else:
                self.client_socket.close()
                break


class TCPServer(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_s.bind(("", port))

        self.server_s.listen(128)

    def run(self):

        while True:
            new_s, client_info = self.server_s.accept()  # 返回一个元组(新的套接字,ip:端口号码)
            print(client_info)
            handle_data_thread = HandleData(new_s)
            handle_data_thread.start()

    def __del__(self):
        self.server_s.close()


tcp_server = TCPServer(7892)
tcp_server.start()
