import socket, json, threading

class server_test():
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__address = ('127.0.0.1', 6000)
        self.client = []
        self.__MAXBYTES = 65535
    def start(self):
        try:
            self.sock.bind(self.__address)
        except:
            print('except Error!')
        print('已成功bind...')
        self.recv()
    def recv(self):
        while True:
            data, address = self.sock.recvfrom(self.__MAXBYTES)
            print('已開啟Thread...') 
            threading.Thread(target=self.handle_message, args=(data, address)).start()
    def handle_text(self, data, address):
        while True:
            # try:
            text = data.decode('utf-8')
            print(f'用戶{address} :{text}')
            self.handle_message(text = text, address = address)
            # except:
            #     print(f'handle message Error! {self.client}')
            #     self.client.pop(address)
            #     break

    def handle_message(self, text, address):
        message = json.loads(text)
        print(f"{message} 's datatype is {type(message)}")
        print(f'The client {address} says: {message} ')
        match message['type']:
            case "1":
                nickname = message['nickname']
                print(nickname)
                cli = {"nickname":nickname, 'address':address}
                self.client.append(cli)

                """
                    為何這邊要有一個x ?
                """
                x = {"type": "2", "isAllow": "Yes"}
                text = json.dumps(x)
                data = text.encode('utf-8')
                self.sock.sendto(data, address)
            
                

server = server_test()
server.start()

