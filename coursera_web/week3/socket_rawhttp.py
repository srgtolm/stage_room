__author__ = 'srgtolm'


import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect (("www.pythonlearn.com", 80))

usr = 'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'
mysock.send(usr)

while True:
    data = mysock.recv(400)
    if len(data) < 1 :
        break
    print data
mysock.close()