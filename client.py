from sys import argv, exit
import socket
from getpass import getpass

def client(host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((host, port))

        output = client.recv(1024)

        command = input(output.decode('utf-8'))
        while command != 'exit':
                client.send(bytes(command, 'utf-8'))
                output = client.recv(4096)
                command = input(output.decode('utf-8'))

def client_setup():
        host = ''
        port = 0

        if '--host' in argv:
                host = argv[argv.index('--host') + 1]
        else:
                exit()
        if '-p' in argv:
                port = int(argv[argv.index('-p') + 1])
        elif '--port' in argv:
                port = int(argv[argv.index('--port') + 1])
        else:
                exit()

        client(host, port)

if __name__ == '__main__':
        client_setup()
