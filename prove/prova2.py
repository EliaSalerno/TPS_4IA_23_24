from tkinter import *
import serial
import time

def close_window():
  global running
  running = False  
  #print( "Window closed")

root = Tk()
root.protocol("WM_DELETE_WINDOW", close_window)
cv = Canvas(root, width=200, height=200)
cv.pack()

arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(1)

running = True;

while running:
    i=int(arduino.readline().decode().strip())
    #print(i)
   
    time.sleep(0.01)
    
    cv.delete("all")
    cv.create_rectangle(10, 10, 20, i,
        outline="#f11", fill="#1f1", width=2)
        
    cv.pack(fill=BOTH, expand=1)
    
    root.update()
    
root.destroy()
arduino.close()
