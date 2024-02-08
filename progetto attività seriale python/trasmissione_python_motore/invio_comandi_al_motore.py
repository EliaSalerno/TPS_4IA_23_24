import serial;
import struct;
ID=b"aa"
MITTENTE=b"0001"
DESTINATARIO=b"0000"
TIPO=b"A1"
VUOTO=b"----------------"

arduino = serial.Serial('COM4', 9600)

print('inizio invio dei dati')
print("+----------------------------+")
print("|  Opzioni per la direzione  |")
print("+----------------------------+")
print("|  Premere D: per la destra  |")
print("+----------------------------+")
print("| Premere S: per la sinistra |")
print("+----------------------------+")
print("|  Premere F: per la fermo   |")
print("+----------------------------+")
print("+-------------------------------------------+")
print("| Velocità                                  |")
print("+-------------------------------------------+")
print("| Minima: 100         | Massimo: 255        |")
print("+-------------------------------------------+")
while True:
    d = input("direzione: ")
    if (d=="F"):
        v=0
    else:
        v = input("velocità: ")
        VELOCITA=str(v).zfill(3).encode()
    DIREZIONE = str(d).zfill(1).encode()
    pack=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO, TIPO, DIREZIONE, VELOCITA, VUOTO)
    arduino.write(pack)
    print(pack)
