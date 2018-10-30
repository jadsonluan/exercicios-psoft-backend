# coding: utf-8
import socket
from threading import Thread

HOST = '' # Endereço IP do servidor
PORT = 5000 # Porta do servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
print "Conectado! Envie uma mensagem."

# Recebe mensagens do servidor enquanto houver conexão.
def read_messages(tcp):
    try:
        response = tcp.recv(1024)
        while (tcp.fileno() != -1) and response:
            print "Server>", response
            response = tcp.recv(1024)
    except:
        pass

th1 = Thread(target=read_messages, args=[tcp])
th1.daemon = True
th1.start()

msg = raw_input()
while True:
    tcp.send (msg)
    if msg == "bye": break
    msg = raw_input()

print "Encerrando conexão com servidor!"
tcp.close()
