# coding: utf-8
import socket
from threading import Thread

HOST = '150.165.42.165'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(5)

connections = []

def read_messages(connection, connections):
    while True:
        con = connection[0]
        msg = con.recv(1024)

        for current_con in connections:
            current_con[0].send(str(connection[1][0]) + " diz: " + msg)

        if msg == "bye":
            con.close()
            connections.remove(connection)

while True:
    print "Esperando conexão ..."
    con, client = tcp.accept()
    print "Conectado por", client
    connections.append((con, client))
    thread1 = Thread(target=read_messages, args=[(con, client), connections])
    thread1.start()
    if (len(connections) == 0): break
