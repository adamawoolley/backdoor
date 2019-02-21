from server_modules.login import login
from server_modules.shell import shell

def client_handler(client, addr):
        shell(client)

#        username, password = client.recv(1024).decode('utf-8').split(':')

##      I can't figure out how to do password authentication
#        if login(username, password):
#                print(f'[*] Successful login for {username} from {addr[0]}:{addr[1]}')
#                ftp_shell = threading.Thread(target=shell,args=(client))
#                ftp_shell.start()
#        else:
#                print(f'[*] Falied login for {username} from {addr[0]}:{addr[1]}')
#                client.send(b'Login Failed')
