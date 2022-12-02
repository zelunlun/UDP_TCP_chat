import socket, json, threading

class server_test():
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__address = ('127.0.0.1', 6000)
        self.client = {}
        self.__MAXBYTES = 65535
        
    def start(self):
        try:
            self.sock.bind(self.__address)
        except:
            print('except Error!')
        print(f'{self.__address} 已成功bind...')
        self.recv()
    def recv(self):
        while True:
            data, address = self.sock.recvfrom(self.__MAXBYTES)     # <- data is a bytes, address is our IP information
            print('已開啟Thread...') 
            threading.Thread(target=self.handle_message, args=(data, address)).start()
    def handle_text(self, data, address):
        # while True:
            # try:
            text = data.decode('utf-8')                  # This step change data(bytes) -> text(string)
            print(f'用戶{address} :{text}')
            self.handle_message(text = text, address = address)
            # except:
            #     print(f'handle message Error! {self.client}')
            #     self.client.pop(address)
            #     break

    def handle_message(self, text, address):
        message = json.loads(text)          # json.loads() is convert string into dictionary
                                            # Here's string is for JSON?
        
        print(f'The client {address} says: {message},  Recive Enter Request!')

        
        match message['type']:
            case 1:
                self.nickname = message['nickname']
                self.client[self.nickname] = address
                
                print(f"Case 1's :{self.client}")
                """
                    因為要確認連接
                """
                x = {"type": 2, "isAllow": True} 
                text = json.dumps(x).encode('utf-8')      # json.dumps() is convert json object to string
                
                self.sock.sendto(text, address)

            case 3:
                msgdic = {
                    'type': 4
                }
                text = json.dumps(msgdic).encode('utf-8')
                self.sock.sendto(text, address)
                msgdic = {
                    'type': 5,
                    'nickname':self.nickname,
                    'message': message['message']
                }                
                text = json.dumps(msgdic).encode('utf-8')
                for client in self.client.values():
                    if client != address:
                        self.sock.sendto(text, client)
                        print(f'Transport {text}, {client}')

server = server_test()
server.start()

