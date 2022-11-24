import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('192.168.115.1', 5050)
s.connect(addr)


def recv_msg():
    print("連接成功！現在可以接收消息！\n")
    while True:
        try:  
            response = s.recv(1024)
            print(response.decode("utf-8"))
        except ConnectionResetError:
            print("服務器關閉，聊天已結束！")
            s.close()
            break


def send_msg():
    print("連接成功！現在可以發送消息！\n")
    print("輸入消息按回車來發送")
    print("輸入esc來退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("utf-8"))

            # ↓為什麼這邊是這樣寫↓
threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()
