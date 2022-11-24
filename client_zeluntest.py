import socket
import threading
import json

class udp_client_chat():
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server_addr = ('127.0.0.1', 6000)
        self.__MAXBYTES = 65535
    def udp_client(self):
        self.sock.bind(('127.0.0.1', 5000))
        # 傳送Enter Request訊息給Server
        x = {"type": "1", "nickname": "大雄"}
        text = json.dumps(x)
        data = text.encode('utf-8')
        self.sock.sendto(data, self.__server_addr)
        # 接收Enter Response訊息
        data, address = self.sock.recvfrom(self.__MAXBYTES)
        message = json.loads(data)
        if message["isAllow"] == "No":
            print("Enter rejected!!")
            exit()
        while(True):
            text = input('Client: input message: ')
            print(f"The {text}'s data type is {type(text)}")
            data = text.encode('utf-8')
            self.sock.sendto(data, self.__server_addr)
            print(f'Client: Sent data: {data}')
            print(f'Client: The OS assigned me the address {self.sock.getsockname()}')

client = udp_client_chat()
client.udp_client()