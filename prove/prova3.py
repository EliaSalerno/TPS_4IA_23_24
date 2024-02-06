from tkinter import *
import tkinter as tk
import serial
import time


def onOff():
    global arduinoOn
    arduinoOn= not arduinoOn
    if arduinoOn:
        arduino.write(b"1")
        bottoneOnOff["bg"]="red"
    else:
        arduino.write(b"0")
        bottoneOnOff["bg"]="#1f1"

def riceviTemperatura(finestra):

    try:
        t=int(arduino.readline().decode().strip())
        temperatura.config(text=str(t))

        cv.delete("all")
        w=cv.winfo_width()/2-10
        cv.create_rectangle(w, 2, w+20, 2+t/4, fill="red", width=2)
        
        cv.pack(fill=BOTH, expand=1)
    finally:    
        finestra.after(10, riceviTemperatura, finestra)    

arduino = serial.Serial('COM9', 9600, timeout=1)

arduinoOn=True

finestra = tk.Tk()
finestra.minsize(300,400)
finestra.title("Sensore di temperatura")

temperatura = tk.Button(finestra, text="0")
bottoneOnOff = tk.Button(finestra, text="ON/OFF", width=30, command=onOff, bg="red")
cv = Canvas(finestra, width=200, height=300)


bottoneOnOff.pack()
temperatura.pack()
cv.pack()

finestra.after(200, riceviTemperatura, finestra)


finestra.mainloop()


