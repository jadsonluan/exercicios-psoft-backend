# coding: utf-8
import socket

host = '192.168.25.39'
port = 5000

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((host, port))
print("Conectado! Enviando request.")

method = raw_input("Qual o método HTTP? ")
url = raw_input("Qual a URL? ")
con.send("%s %s HTTP/1.0" % (method, url))
response = con.recv(1024)
print(response)
response = con.recv(1024)
print(response)