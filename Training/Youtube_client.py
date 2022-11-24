import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.115.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send():
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.sendall(send_length)
    client.sendall(message)
    
    while True:
        msg = input()
        if msg == "0":
            print("你退出了聊天")
            send(DISCONNECT_MESSAGE)
            break
        client.send(msg.encode("gbk"))
    
def recv_msg():
    print('現在可以接受消息')
    while True:
        try:  # 測試發現，當服務器率先關閉時，這邊也會報ConnectionResetError
            response = client.recv(1024)
            print(response.decode("gbk"))
        except ConnectionResetError:
            print("服務器關閉，聊天已結束！")
            client.close()
            break

threads = [threading.Thread(target=recv_msg), threading.Thread(target=send)]
for t in threads:
    t.start()
while(True):
    text = input()
    send(text)
        # sendto( bytes, tuple(要有IP, port)) 
        # bytes→ BYTE的array
    print(f'Sent data: {text}')