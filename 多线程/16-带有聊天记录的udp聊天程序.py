
import socket
import threading
import queue


class SendMsg(threading.Thread):

    def __init__(self, udp_socket, queue):
        super().__init__()
        self.udp_socket = udp_socket
        self. queue = queue

    def run(self):
        """获取键盘数据，并将其发送给对方"""
        while True:
            print("1: 发送数据")
            print("2: 退出程序")
            op = input("请输入操作序号:")
            if op == "1":
                # 1. 输入对方的ip地址
                dest_ip = input("\n请输入对方的ip地址:")
                # 2. 输入对方的port
                dest_port = int(input("\n请输入对方的port:"))
                while True:
                    # 3. 从键盘输入数据
                    msg = input("\n请输入要发送的数据:")
                    if msg:
                        # 4. 发送数据
                        self.udp_socket.sendto(msg.encode(
                            "utf-8"), (dest_ip, dest_port))
                        info = "<<<(%s, %d):%s\n" % (dest_ip, dest_port, msg)
                        self.queue.put(info)
                    else:
                        # 要是没有输入内容则认为是要重新输入ip、port
                        break
            elif op == "2":
                break

    def __del__(self):
        self.udp_socket.close()


class RecvMsg(threading.Thread):
    def __init__(self, udp_socket, queue):
        super().__init__()
        self.udp_socket = udp_socket
        self.queue = queue

    def run(self):
        """接收数据并显示"""
        while True:
            try:
                # 1. 接收数据
                recv_msg = self.udp_socket.recvfrom(1024)
            except:
                break
            else:
                # 2. 解码
                recv_ip = recv_msg[1]
                recv_msg = recv_msg[0].decode("utf-8")
                # 3. 显示接收到的数据
                info = ">>>%s:%s\n" % (str(recv_ip), recv_msg)
                print(info)
                self.queue.put(info)

    def __del__(self):
        self.udp_socket.close()


class SaveChat(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            with open("./chat.txt", "a") as f:
                chat_info = self.queue.get()
                print("正在将(%s)写入到聊天记录文件中" % chat_info)
                f.write(chat_info)


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 7891))

    # 创建一个FiFo的队列
    q = queue.Queue()

    # 创建线程对象
    udp_r = RecvMsg(udp_socket, q)
    udp_s = SendMsg(udp_socket, q)
    chat_thread = SaveChat(q)

    # 运行创建的子线程
    udp_r.start()
    udp_s.start()
    chat_thread.start()


if __name__ == "__main__":
    main()
