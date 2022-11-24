import threading
import socket
MAX_BYTES = 65535
remote_addr = ('127.0.0.1',3506) # Remote server address
bind_addr = ('127.0.0.1', 6666)  # local bind address
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Client thread function
def udp_client(remote_addr):
    while(True):
        try:
            text = input('input message: ')
        except:
            print(f'client_handle Error!')
            pass
        data = text.encode('utf-8')
        sock.sendto(data, remote_addr)
        print('Sent data: {}'.format(data))
        print('The OS assigned me the address {}'.format(sock.getsockname()))
def udp_server(bind_addr):
    sock.bind(bind_addr)
    print('Listening at {}'.format(sock.getsockname()))
    while(True):
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print('The client at {} says {!r}'.format(address, text))
thread_server = threading.Thread(target=udp_server, args=(bind_addr,))
thread_client = threading.Thread(target=udp_client, args=(remote_addr,))
thread_client.start()
thread_server.start()
thread_server.join()
thread_client.join()
print('Done.')
