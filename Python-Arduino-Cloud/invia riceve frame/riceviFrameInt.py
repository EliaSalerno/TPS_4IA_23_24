import serial
import struct
packetFormat="<2s I I B H 19s"
packetFields=("packetID","mittente","destinatario","tipo","valoreSensore","vuoto")
#-------------------------------------------------------------------------------
# configura seriale
#-------------------------------------------------------------------------------
ser = serial.Serial('COM3',9600)
#-------------------------------------------------------------------------------
# lettura dato
#-------------------------------------------------------------------------------
while True:
     if ser.in_waiting>=32:
        buffer=ser.read(32)
        splittedBuffer=struct.unpack(packetFormat,buffer)
        myPacket=dict(zip(packetFields,splittedBuffer))
        print(myPacket)
        if myPacket["packetID"].decode()=="EP":
            if myPacket["destinatario"]==2:
               print(myPacket["valoreSensore"])
