from sys import argv
from server_modules.run_server import run_server

def server_setup():
        host = '127.0.0.1'
        port = 3500

        if '-p' in argv:
                port = int(argv[argv.index('-p') + 1])
        elif '--port' in argv:
                port = int(argv[argv.index('--port') + 1])
        if '--host' in argv:
                host = argv[argv.index('--host') + 1]

        print(f'[*] Listening on {host}:{port}')

        run_server(host, port)

if __name__ == '__main__':
        server_setup()
