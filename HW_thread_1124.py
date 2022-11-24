import threading
import socket
# MAX_BYTES = 65535
# remote_addr = ('127.0.0.1',6000) # Remote server address
# bind_addr = ('127.0.0.1', 5000)  # local bind address
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

class udp_client_room():
    def __init__(self) -> None:
        self.remote_addr = ('127.0.0.1', 6000)
        self.bind_addr = ('127.0.0.1', 5000)
        self.MAX_BYTES = 65535
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def udp_server(self):
        self.sock.bind(self.bind_addr)
        print('Listening at {}'.format(self.sock.getsockname()))
        while(True):
            data, address = self.sock.recvfrom(self.MAX_BYTES)
            text = data.decode('utf-8')
            print(f'The client at {address} says {text}')
    def udp_client(self):
        while(True):
            try:
                text = input('input message: ')
            except:
                print(f'client_handle Error!')
                pass
            data = text.encode('utf-8')
            self.sock.sendto(data, self.remote_addr)
            print('Sent data: {}'.format(data))
            print('The OS assigned me the address {}'.format(self.sock.getsockname()))
    # def thread_start(self):
    #     thread_server = threading.Thread(target=self.udp_server, args=(self.bind_addr,))
    #     thread_client = threading.Thread(target=self.udp_client, args=(self.remote_addr,))
    #     thread_client.start()
    #     thread_server.start()

    # def thread_end(self):
    #     self.thread_server.join()
    #     self.thread_client.join()

client = udp_client_room()
client.udp_server()
client.udp_client()





# Client thread function
# def udp_client(remote_addr):
#     while(True):
#         try:
#             text = input('input message: ')
#         except:
#             print(f'client_handle Error!')
#             pass
#         data = text.encode('utf-8')
#         sock.sendto(data, remote_addr)
#         print('Sent data: {}'.format(data))
#         print('The OS assigned me the address {}'.format(sock.getsockname()))
# def udp_server(bind_addr):
#     sock.bind(bind_addr)
#     print('Listening at {}'.format(sock.getsockname()))
#     while(True):
#         data, address = sock.recvfrom(MAX_BYTES)
#         text = data.decode('utf-8')
#         print('The client at {} says {!r}'.format(address, text))


# thread_server = threading.Thread(target=udp_server, args=(bind_addr,))
# thread_client = threading.Thread(target=udp_client, args=(remote_addr,))
# thread_client.start()
# thread_server.start()
# thread_server.join()
# thread_client.join()
# print('Done.')
