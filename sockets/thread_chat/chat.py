import socket
import codecs
from caesar_cipher import *
from threading import Thread, Lock

def send(s, sema):
    msg = input("Enter a message: " )   
    msg_as_bytes = codecs.encode(cod_cesar(msg, CAESAR_KEY))
    s.sendall(msg_as_bytes)
    print('Sent: ', msg)
    sema.release()

def receive(s, sema):
    data = s.recv(1024)
    sema.release()
    print('Received: ', decod_cesar(codecs.decode(data), CAESAR_KEY))
