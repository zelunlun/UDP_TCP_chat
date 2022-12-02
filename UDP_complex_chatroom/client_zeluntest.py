import socket
import threading
import json


MAX_BYTES = 65535
server_addr = ('127.0.0.1',6000) # Remote server address
# 執行緒send_message()：取得使用者的輸入訊息字串，將其傳送到Server
def send_message():
    print('執行緒send_message開始')
    while(True):
        msg = input("請輸入訊息: ")

        #  離開
        if msg == "esc":
            msgdic = {
            'type':7,
            'nickname':nickname
            }
            text = json.dumps(msgdic).encode('utf-8')
            sock.sendto(text, server_addr)    
            break
        
        msgdic = {
            'type':3,
            'nickname':nickname,
            'message':msg
        }
        text = json.dumps(msgdic).encode('utf-8')
        sock.sendto(text, server_addr)
        
# 執行緒recv_message()：    
def recv_message():
    print('執行緒recv_message開始') 
    while(True):
        data, address = sock.recvfrom(MAX_BYTES)
        msgdict = json.loads(data.decode('utf-8'))
        match  msgdict['type'] :
            case 4:
                print("Here is Case 4!")
                pass
            case 5:
                print(f"{msgdict['nickname']} says : {msgdict['message']}")
            case 8:
                print(f"{msgdict['message']}")

# 請使用者輸入他的nickname
nickname = input('請輸入你留言時的綽號/別名：')
# 建立一個UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 準備Enter Request訊息的dict物件
msgdict = {
"type": 1,
"nickname": nickname
}
# 轉成JSON字串，再轉成bytes
data = json.dumps(msgdict).encode('utf-8')
# 將Enter Request送到Server
sock.sendto(data, server_addr) 

# 等待並接收Server傳回來的訊息，若為Enter Response則繼續下一步，否則繼續等待
is_entered = False
while not is_entered:
    data, address = sock.recvfrom(MAX_BYTES)
    msgdict = json.loads(data.decode('utf-8'))
    
    if msgdict['isAllow'] == True:
        is_entered = True
        print('成功進入伺服器!!!, Receive Enter Response!')
# 建立兩個threads：send_message與recv_message
thread_send_message = threading.Thread(target=send_message)
thread_recv_message = threading.Thread(target=recv_message)
thread_send_message.start()
thread_recv_message.start()
thread_send_message.join()
thread_recv_message.join()
print('程式結束')



























# class udp_client_chat():
#     def __init__(self) -> None:
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.__server_addr = ('127.0.0.1', 6000)
#         self.__MAXBYTES = 65535
#     def send_message(self):
#         while True:
#             try:
#                 nickname = 
#             except:
#                 print(send_message)
# client = udp_client_chat()
# client.udp_client()





    # def udp_client(self):
    #     self.sock.bind(('127.0.0.1', 5000))
    #     # 傳送Enter Request訊息給Server
    #     x = {"type": "1", "nickname": "大雄"}
    #     text = json.dumps(x)
    #     data = text.encode('utf-8')
    #     self.sock.sendto(data, self.__server_addr)
    #     # 接收Enter Response訊息
    #     data, address = self.sock.recvfrom(self.__MAXBYTES)
    #     message = json.loads(data)
    #     if message["isAllow"] == "No":
    #         print("Enter rejected!!")
    #         exit()
    #     while(True):
    #         text = input('Client: input message: ')
    #         print(f"The {text}'s data type is {type(text)}")
    #         data = text.encode('utf-8')
    #         self.sock.sendto(data, self.__server_addr)
    #         print(f'Client: Sent data: {data}')
    #         print(f'Client: The OS assigned me the address {self.sock.getsockname()}')