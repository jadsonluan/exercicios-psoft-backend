import socket
from threading import Thread
HOST = '150.165.42.165'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

def read_messages(tcp):
    while True:
        response = tcp.recv(1024)
        print response

th1 = Thread(target=read_messages, args=[tcp])
th1.start()

print "Conectou"
msg = raw_input()
while msg != "bye":
    tcp.send (msg)
    msg = raw_input()
tcp.close()
