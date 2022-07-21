import socket

host='datadog.com'
port=514
message='hello world\n'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.sendall(message)
s.close()
