import socket
import threading
import os


class ChatSever:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (socket.gethostbyname(socket.gethostname()), 5050)
        self.users = {}
        self.FORMAT = "utf-8"

    def start_sever(self):
        try:
            self.sock.bind(self.addr)
        except:
            print('Error!')    
        self.sock.listen(5)
        print("服務器已開啓，等待連接...")
        print("在空白處輸入stop sever並回車,來關閉服務器")
        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print(f"用戶{addr}連接成功！現在共有{number}位用戶")

            threading.Thread(target=self.recv_send, args=(s, addr)).start()
        
    def recv_send(self, sock, addr):
        while True:
            try:  # 測試後發現，當用戶率先選擇退出時，這邊就會報ConnectionResetError
                response = sock.recv(4096).decode(self.FORMAT)
                msg = f"用戶{addr}發來消息：{response}"

                for client in self.users.values():
                    client.send(msg.encode(self.FORMAT))
            except ConnectionResetError:
                print(f"用戶{addr}已經退出聊天！")
                self.users.pop(addr)
                for client in self.users.values():
                    client.sendall(f"用戶{addr}已經退出聊天！".encode(self.FORMAT))
                break

    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()


if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()