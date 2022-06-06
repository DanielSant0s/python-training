from chat import *

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port to listens on

sema = Lock()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST, PORT))
ss.listen()
print("Listen ip:" + HOST + " port: " + str(PORT))

s, addr = ss.accept()
info = socket.getnameinfo(addr, socket.NI_NUMERICSERV)

print("Connected by ", info)

while True:
    sema.acquire()
    recv_thd = Thread(target=receive, args=(s, sema))
    recv_thd.start()
    sema.acquire()
    send_thd = Thread(target=send, args=(s, sema))
    send_thd.start()
