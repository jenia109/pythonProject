import socket


clients = []
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.bind(('localhost', 9090))

close_program = False
print('server start')

while not close_program:
    try:
        data, addr = my_socket.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        print(data, addr)
        for client in clients:
            if addr != client:
                my_socket.sendto(data, client)

    except Exception as e:
        print(e)
        print('Server stopped')
        close_program = True

my_socket.close()

