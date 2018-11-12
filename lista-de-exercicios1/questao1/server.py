import socket, os

cwd = os.getcwd()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
s.close()
port = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origin = (host, port)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp.bind(origin)
tcp.listen(1)

def trata_request(request):
    data = request.split()
    response = "400"
    if (len(data) == 3):
        method = data[0]
        url = os.getcwd() + data[1]
        filename = url[1:]
        http_v = data[2]

        if method == 'GET':
            if os.path.isfile(url):
                print "Solicitando", url
                with open(url, 'r') as content_file:
                    response = content_file.read()
            else:
                resposne = "404"
        else:
            response = "405"

    return response

def wait_request(tcp):
    con, client = tcp.accept()
    request = con.recv(1024)

    if request:
        content = trata_request(request)
        # con.send("HTTP/1.0 %d OK\r\n" % code)
        con.send("X-projsw: 117110391\r\n")
        con.send(content + "\r\n")
    con.close()

print "Ouvindo em", host, port
while True:
    wait_request(tcp)