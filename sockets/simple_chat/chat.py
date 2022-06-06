import socket
import codecs
from caesar_cipher import *

def send(s):
    msg = input("Enter a message: " )   
    msg_as_bytes = codecs.encode(cod_cesar(msg, CAESAR_KEY))
    s.sendall(msg_as_bytes)
    print('Sent: ', msg)

def receive(s):
    data = s.recv(1024)
    print('Received: ', decod_cesar(codecs.decode(data), CAESAR_KEY))
