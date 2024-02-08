import time
import struct
import serial

ID="aa"
DESTINATARIO="0000"
FORMATO='2s 4s 4s 2s 4s 16s'

arduino=serial.Serial('COM3',9600)
time.sleep(1)
print("In attesa...")

id="aa"
mittente="0000"
destinatario="0000"
tipo="aa"
valoreSensore="0000"
vuoto="................"
while True:
    print(arduino.in_waiting)
    if arduino.in_waiting>31:
        buffer_dati=arduino.read(32)
        buffer=struct.unpack(FORMATO,buffer_dati)
        id=buffer[0].decode()
        mittente=buffer[1].decode()
        destinatario=buffer[2].decode()
        tipo=buffer[3].decode()
        valoreSensore=buffer[4].decode()
        vuoto=buffer[5].decode()
        if id==ID and destinatario==DESTINATARIO:
            print("Mittente: "+mittente)
            print("Destinatario: "+destinatario)
            print("Tipologia: "+tipo)
            print("Valore ricevuto: "+valoreSensore)
            print(vuoto)
        buffer_dati=b''
    time.sleep(0.9)
