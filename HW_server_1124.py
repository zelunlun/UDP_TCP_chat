import socket
import json


class udp_server():
    def __init__(self) -> None:
        self.__port = 6000
        self.client = []
        self.__MAX_BYTES = 65535
        self.__ip = "127.0.0.1"
        self.data = "1"
        self.address = ("123","1")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def bind(self):
        
        self.sock.bind((self.__ip, self.__port))
        self.recvfrom()
    def recvfrom(self):
        # while True:
        #     self.data , self.address = sock.recvfrom(self.__MAX_BYTES)
            
        #     text = data.decode('utf-8')
        #     print(f'The client at {self.address} says {text}')
        #     message = json.loads(text)
        #     match message['type']:
        #         case 1:
        #             nickname = message['nickname']
        #             client_dict = {'nickname': nickname, 'address': self.address}
        #             self.client.append(client_dict)
        #         case 2:
        while(True):
            # 接收來自client的訊息
            data, address = self.sock.recvfrom(self.__MAX_BYTES)
            print(f'{data}, {address} is connect!')
            text = data.decode('utf-8')
            print(f'The client at {address} says {text}')
            # 轉成dictionary物件
            message = json.loads(text)
            # 依照type欄位的值做對應的動作
            if message["type"] == 1:
                # 取出nickname欄位
                nickname = message["nickname"]
                print(nickname)
                # 在client_list中加入一筆client資訊的dict物件
                cli = {"nickname": nickname, "address": address}
                self.client.append(cli)
                # 送回Enter Response訊息給Client
                x = {"type": 2, "isAllow": "Yes"} #<- 這行在幹嘛???
                text = json.dumps(x)
                data = text.encode('utf-8')
                self.sock.sendto(data, address)

server = udp_server()
server.bind()





# MAX_BYTES = 5     # 一次最多收幾個BYTE
# my_port = 6000
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(("127.0.0.1", my_port))
# # print(socket.getnameinfo(("0.0.0.0", my_port), 0))  # 我可以用這行來知道連線的數量嗎
# # print(f'Listen at {sock.getsockname()}')
# while True:
#     # try:
#         data, address= sock.recvfrom(MAX_BYTES)
#         text = data.decode('utf-8')            
#         print()
        
#         convert_fromtext = json.loads(text)
    



    # except:
    #     print('This is an except Error')
    #     break
    # if text == 'abc':
    #     sock.close()
    #     break
        # print(f'The client at {address} says {text}')


