import socket

client_port = 3506
server_port = 6666
BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',0))                      # 原本client端設為 3506 會報錯
while True:
    try:
        sock.connect(('127.0.0.1', server_port))
        data, address = sock.recvfrom(BYTES)
    except:
        print('Error')
        break
    print(data)
    print(address)
    my_input = input()
    