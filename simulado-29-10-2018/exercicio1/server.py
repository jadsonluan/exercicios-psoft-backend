# coding: utf-8
import socket
from threading import Thread

HOST = '' # Endereço IP do servidor
PORT = 5000 # Porta do servidor
num_connections = 5 # número máximo de conexões

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Opção para permitir reuso do endereço de IP após fechamento
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(num_connections)

# Método que recebe mensagens de determinado cliente e envia a mesma mensagem de
# volta para todos os clientes conectados ao servidor.
def read_messages(client, connections):
    connection = client[0]
    client_ip = client[1][0]

    # Enquanto houver conexão ...
    msg = connection.recv(1024)
    while msg != "bye":
        for current_client in connections:
            current_client[0].send(msg)
        msg = connection.recv(1024)

    print "O cliente", client_ip, "desconectou-se!"
    print "Atualmente há", len(connections) - 1, "cliente(s) conectados!"
    print ""

    connection.close()
    connections.remove(client)

connections = []

# Aceita uma conexão com o servidor e em seguida cria um thread de tratamento de
# mensagens para ela.
def accept_client(tcp, connections):
    print "Esperando conexão [...]"
    con, client = tcp.accept()
    connections.append((con, client))

    print "Conectado por", client
    print "Atualmente há", len(connections), "cliente(s) conectados!"
    print ""

    thread = Thread(target=read_messages, args=[(con, client), connections])
    thread.daemon = True
    thread.start()

# Itera a aceitação de conexões
def loop_accept(tcp, connections):
    while True:
        accept_client(tcp, connections)


# cliente inicial
accept_client(tcp, connections)

# Cria e executa daemon/thread para aceitar conexões de forma paralela
# Importante ser daemon, pois ao finalizar o programa, todos os daemon
# são finalizados
client_threads = Thread(target=loop_accept, args=[tcp, connections])
client_threads.daemon = True
client_threads.start()

# Para que o programa continue rodando enquanto houver clientes conectados!
while len(connections) != 0:
    pass

tcp.close()
