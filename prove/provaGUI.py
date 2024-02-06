import tkinter

def bottoneClick():
    print(5)

finestra = tkinter.Tk()
finestra.minsize(300,100)
finestra.title("Prova")

bottone = tkinter.Button(finestra, text="clicca",command=bottoneClick)

bottone.pack()

finestra.mainloop()


