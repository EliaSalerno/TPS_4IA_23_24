# ELENCO COMANDI A CASO PER RIPASSARE/STUDIARE PYTHON

# Si usa per commentare
#per importare funzioni non presenti nella libreria standard di python
import random

#definizione funzione con passaggio parametri
def saluto(nome,cognome):
    global p #DICHIARAZIONE VARIABILE GLOBALE
    p="pirla"
    x=4
    print("ciao ",nome,cognome)

#assegnazione multipla a variabili
x,y,z=str(0),int(0),float(0)
print("Hello world!")
if 5>2:
    print(type(x)) #stampa del tipo della variabile
    print(type(y))
    print(type(z))
    print(x," ",y," ",z) #stampa multipla di più variabili di tipo diverso
#l'operatore + va usato solo tra variabili del medesimo tipo

#assegnazione di un valore a più variabili    
a=b=c="prova"
if a==b:
    if a==c:
        d=" è uguale a "
    else:
        d=" è diverso da "
else:
    d=" è stranamente diverso da "
print(b,d,c)

#creazione lista e spacchettamento di una lista per assegnare i valori a variabili
studente =["Elia Donato","Salerno","00012"]
nome,cognome,matricola=studente
print("nome = ",nome)
print("cognome = ",cognome)
print("matricola = ",matricola)
saluto(nome,cognome)
p=p+" o no?" #variabile creata come globale nella definizione della funzione sopra
x="sei un"
print(x,p)

#creazione di un dizionario
docente={"name":"Elia Donato","surname":"Salerno","age":34}
print(docente["name"])

#la funzione random importata all’inizio
print(random.randrange(1,10))

#assegnazione di più stringhe con i tripli apici singoli o doppi
n="""+------+------------+
| nome |"""
print(n,nome) #per vedere cosa succede provare a stampare l’output di tutto ciò presente nel pdf

# le stringhe sono array

a="Ciao a tutti"
print(a[1])

for x in "Ciao":
    print(x)
    print(" ")

a="+------+-"
b="| nome | "
for x in nome:
    a=a+"-"
a=a+"-+"
print(a)
print(b+nome+" |")
print(a)
