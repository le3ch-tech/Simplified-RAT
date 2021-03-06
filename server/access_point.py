import socket
import os
from os import system


class main:
    def clear_():
        if os.name == 'nt':
            clear_ = 'clr'
            return clear_
        else:
            clear_ = 'clear'
            return clear_

    def start_server():
        global server_socket
        global port
        port = 80
        max_connections_allowed = 1
        server_socket = socket.socket(socket.AFINET, socket.SOCKSTREAM)
        host = socket.gethostname()
        server_socket.bind((host, port))
        server_socket.listen(max_connections_allowed)
        
        os.system(clear_())
    
    def connections():
        global client_socket
        client_socket, addr = server_socket.accept()
        print('Connection from {}'.format(str(addr)))
        
    def message():
        global msg
        msg = input()
        if msg == 'help':
            system.os(clear_())
            print("{}HELP{}".format(6*'*'), (6*'*'))
            print("Test Connection: 'test'")
        else:
            msg = msg.encode("UTF-8")
            client_socket.send(msg)
            msg = client_socket.recv(4096)
            print(msg.decode("UTF-8"))
            
'''if __name__ == '__main__':
    let = main()
    let.operating_system()
    let.start_server()
    let.connections()
    let.message()    '''
