import socket
import threading
from server_modules.client_handler import client_handler

def run_server(host, port):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((host, port))

        server.listen(5)

        while True:
                client,addr = server.accept()

                print(f'[*] Accepted connection from: {addr[0]}:{addr[1]}')

                handle_client = threading.Thread(target=client_handler,args=(client,addr))
                handle_client.start()
