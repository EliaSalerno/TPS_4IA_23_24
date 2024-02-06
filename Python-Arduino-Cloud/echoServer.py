# Programma server Echo 
import socket

HOST = ''                                   # host locale     
PORT = 50010                                # porta di ascolto
                                            
s = socket.socket()                         # creazione oggetto socket
s.bind((HOST, PORT))                        # associazione alla porta
s.listen()                                  # messa in ascolto sulla porta

while True:
    print("Attendo richieste di connessione ....")            
    conn, addr = s.accept()                 # attesa richiesta connessione
    print ('Connesso da ', addr)            # richiesta accettata

    while True:
        print ("Attendo messaggi ...")
        data = conn.recv(1024)              # attesa messaggi
        if not data: 
            break
        print("Ricevuto: ",data.decode())   # messaggio ricevuto
        conn.send(data)
    print("Connessione chiusa")             # connessione chiusa dal client
    conn.close()
