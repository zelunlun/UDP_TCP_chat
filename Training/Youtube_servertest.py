
"""
    這個Project 沒做到的東西↓
    1. 一直開著讓client無限輸入
    2. 讓Client互相看到對方打了什麼
"""

import socket 
import threading

PORT = 5050
# SERVER = '10.101.196.195' 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
"""
    gethostbyname 是在做找尋本電腦IPv4 的動作- 192.168.1.0
    gethostname   是在找本台主機的名稱       - LAPTOP-U434QEBC    
"""
HEADER = 64
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
user = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def client_handle(conn, addr):

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)       # <- 這裡就是所謂的阻塞代碼行，如果Client不輸入東西我們就沒辦法繼續下去
        except:                                                 #    所以才需要 Multi-thread 讓程式可以讀別人的
            print(f'client_handle Error!')
            continue
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        # print(f'This person {addr} says : {msg}')
        
        for client in user.values():
            client.sendall(msg.encode(FORMAT))
        if msg == DISCONNECT_MESSAGE:
            connected = False

            conn.send(f"The person {addr} is leave".encode(FORMAT))

    conn.close()
    while connected:
        msg_length = conn.recv()    


def start():
    server.listen()
    while True:
        conn, addr = server.accept()    # 在這行會先凍結，等到連線近來
        user[addr] = conn
        # conn 是 socket單元
        # addr 是 client的PORT是多少呀，IP多少等訊息
        thread = threading.Thread(target=client_handle, args=(conn, addr))      # 後面的args是什麼意思
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1} , The args are {conn, addr}")
        

print(f"[STARTING] server is starting ...")
# thread.join()
start()
