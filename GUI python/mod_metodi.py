import serial
import struct
import time
import serial.tools.list_ports
import prova 

def main():
    prova.lsdevice()
#    porta=pdevice()
#    print(porta)
#    arduino=serial.Serial(porta,9600)
#    pacchetto=struct.unpack('2s 4s 4s 2s 4s 16s',arduino.read(32))
#    print(pacchetto)
#    metodi richiamato da modulo prova solo per test
#    print(prova)
    prova.saluto(4)
#def pdevice():
#    ports=serial.tools.list_ports.comports()
#    listPort=[]
#    for port in sorted(ports):
#        listPort.append(port)
#    if len(listPort)>0:
#        return listPort[0].name
#        for i in listPort:
#            print(i.name)
#            print(i.description)
            


if __name__=="__main__":
    main()
