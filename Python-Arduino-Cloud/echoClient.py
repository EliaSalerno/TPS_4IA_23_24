# Programma client Echo
import socket

HOST = '127.0.0.1'                  # indirizzo del server
PORT = 50010                        # porta del serve

s = socket.socket()                 # reazione oggetto socket
s.connect((HOST, PORT))             # apertura della socket

s.send(('Hello, world').encode())   # invio messaggio
data = s.recv(1024)                 # attesa e ricezione risposta
print ('Ricevuto:', data)

s.close()                           # chiusura connessione
