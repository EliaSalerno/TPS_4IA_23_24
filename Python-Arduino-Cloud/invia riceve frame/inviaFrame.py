import serial
import time
import struct
ID=b"EP"
MITTENTE=b"P001"
DESTINATARIO=b"A328"
TIPO=b"A1"
VUOTO=("."*16).encode()
#-------------------------------------------------------------------------------
# configura seriale
#-------------------------------------------------------------------------------
ser = serial.Serial('COM3',9600)
#-------------------------------------------------------------------------------
# invio dato (invia numeri in progressione)
#-------------------------------------------------------------------------------
i=0
while True:
    direzione=b"A"
    velocita=str(i).zfill(3).encode()
    msg=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO,TIPO,direzione,velocita,VUOTO)
    ser.write(msg)
    print(msg)
    i+=1
    time.sleep(5)