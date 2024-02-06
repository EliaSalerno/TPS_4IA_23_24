import tkinter

# funzione che viene chiamata ogni secondo
def scatta(finestra):
    s=int(secondi["text"])+1
    secondi.config(text=s)
    finestra.after(1000, scatta, finestra)    #richiamo della funzione dopo un secondo

finestra = tkinter.Tk()
finestra.title("Prova")

secondi=tkinter.Label(finestra,text="0")
secondi.grid(row=0,column=0)

finestra.after(1000, scatta, finestra) #richiamo della funzione dopo un secondo

finestra.mainloop()


