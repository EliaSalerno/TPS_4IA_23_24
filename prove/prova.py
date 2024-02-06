import serial

import time

arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(1)
while True:
    print("--------")
    l=arduino.readline()
    print(l)
    s=l.decode()
    print(s)
    t=s.strip()
    print(t)
    i=int(t)
    print(i)
   
    time.sleep(0.01)
