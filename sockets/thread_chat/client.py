from chat import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

sema = Lock()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print ("Successful connection. ")

while True:
    sema.acquire()
    send_thd = Thread(target=send, args=(s, sema))
    send_thd.start()
    sema.acquire()
    recv_thd = Thread(target=receive, args=(s, sema))
    recv_thd.start()
    