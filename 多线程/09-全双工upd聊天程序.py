import socket
import threading


def send_msg(udp_socket):
    while True:

        dest_ip = input("\n请输入对方的ip地址:")
        dest_port = int(input("\n请输入对方的port:"))
        while True:
            msg = input("\n请输入要发送的数据:")
            if msg:
                udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))
            else:
                break


def recv_msg(upd_socket):
    while True:
        recv_msg = upd_socket.recvfrom(1024)
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    upd_socket.bind(("", 7892))
    send_msg_t = threading.Thread(target=send_msg, args=(upd_socket,))
    recv_msg_t = threading.Thread(target=recv_msg, args=(upd_socket,))
    send_msg_t.start()
    recv_msg_t.start()

    # 主线程浪费了,理解深入之后可以只创一个子线程,另一个放在主线程跑
if __name__ == "__main__":
    main()
