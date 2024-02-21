import time
import struct
import serial
import prova
import tkinter as tk

#dx=100
#dy=100
FORMATO="2S 4S 4S 2S 4S 16S"
window=tk.Tk()
#window.geometry(str(dx)+"x"+str(dy))
window.title("Hello world!")
#window.resizable(False,False)
window.configure(background="white")

def portlist():
    listPort=[]
    listPort=prova.lsdevice()
    lp=[]
    for i in range(len(listPort)):
        lp.append(listPort[i].name)

    porte=tk.Variable(value=lp)
    listbox=tk.Listbox(
        window,
        listvariable=porte,
        height=2,
        selectmode=tk.EXTENDED
    )
#    listbox.pack(expand=True,fill=tk.BOTH)
    listbox.grid(row=0,column=1)

def conSensor():
    arduino=prova.sfind("R")
    max=arduino.in_waiting
    arduino.read(max)
    while True:
        if arduino.in_waiting>31:
            buffer=struct.unpack('2s 4s 4s 2s 4s 16s',arduino.read(32))
            valSensore=buffer[4].decode()
            print(valSensore)
            text_output=tk.Label(window,text=valSensore)
            text_output.grid(row=1,column=1)
            time.sleep(0.9)

first_button=tk.Button(text="Elenca porte",command=portlist)
first_button.grid(row=0,column=0)
second_button=tk.Button(text="Collega sensore",command=conSensor)
second_button.grid(row=1,column=0)

if __name__=="__main__":
    window.mainloop()
