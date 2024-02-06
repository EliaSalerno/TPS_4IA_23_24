import serial
import struct
MIO_ID=b"EP"
MIO_INDIRIZZO=b"P001"
MIO_TIPO=b"S1"
#-------------------------------------------------------------------------------
# configura seriale
#-------------------------------------------------------------------------------
ser = serial.Serial('COM3',9600)
#-------------------------------------------------------------------------------
# lettura dato
#-------------------------------------------------------------------------------
while True:
     if ser.in_waiting>=32:
        msg=(struct.unpack("2s 4s 4s 2s 4s 16s",ser.read(32)))
        print(msg)
        id=msg[0]
        if id==MIO_ID:
            mittente=msg[1]
            destinatario=msg[2]
            if destinatario==MIO_INDIRIZZO:
               tipo=msg[3]
               if tipo==MIO_TIPO:                  
                  valoreSensore=int(msg[4])
                  print(valoreSensore)
               else:
                  print("Errore - ricevuto tipo "+tipo)