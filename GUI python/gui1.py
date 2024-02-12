import tkinter as tk

window=tk.Tk()
window.geometry("600x600")
window.title("Hello world!")
window.resizable(False,False)
window.configure(background="white")

def first_print():
    text="Hello world!"
    text_output=tk.Label(window,text=text,fg="red",font=("Helvetica",16))
    text_output.grid(row=0,column=1,sticky="W")

def second_print():
    text="Nuovo messaggio! Nuova funzione!"
    text_output=tk.Label(window,text=text,fg="green",font=("Helvetica",16))
    text_output.grid(row=1,column=1,padx=50)
    
first_button=tk.Button(text="Saluta!",command=first_print)
first_button.grid(row=0,column=0)
second_button=tk.Button(text="Seconda funzione",command=second_print)
second_button.grid(row=1,column=0,pady=20,padx=5)
