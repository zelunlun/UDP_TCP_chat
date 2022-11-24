"""
    這邊是只有傳的部分
"""
if __name__ == '__main__':
    import socket
    server_port = 3506
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                        # AF_INET→ 指定ipv4協定的const  DGARM是UDP的一個種類
                        # AF的F 是Family的意思
                        # sock→ return object 
    while(True):
        text = input()
        data = text.encode('utf-8')
        sock.sendto(data,('172.20.10.2',server_port))
            # sendto( bytes, tuple(要有IP, port)) 
            # bytes→ BYTE的array
        print(f'Sent data: {data}')
        print(f'The OS assigned me the address {sock.getsockname()}')
        
"""
    以下是Server
"""

import socket
MAX_BYTES = 5     # 一次最多收幾個BYTE
my_port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", my_port))
print(socket.getnameinfo(("0.0.0.0", my_port), 0))  # 我可以用這行來知道連線的數量嗎
print(f'Listen at {sock.getsockname()}')
while True:
    # try:
        data, address= sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')              # UTF-8沒辦法自動去判斷
                                                 # 把它改成Big5就可以了
    # except:
    #     print('This is an except Error')
    #     break
    # if text == 'abc':
    #     sock.close()
    #     break
        print(f'The client at {address} says {text}')
    