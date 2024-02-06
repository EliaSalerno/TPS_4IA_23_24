# Decoratori
import time

def tempo(funzione):

    def busta(*args, **kwargs):
        import time
        t1 = time.time()
        result = funzione(*args, **kwargs)
        t2 = time.time() - t1
        print("Tempo esecuzione di " + funzione.__name__ + ": " + str(t2))
        return result

    return busta

def prova(x,y):
    time.sleep(1)
    print(x*y)

def prova1(m):
    time.sleep(2)
    print(m)

@tempo
def prova2(a,b):
    time.sleep(1)
    print(a+b)

    
prova=tempo(prova)
prova(3,4)

prova1=tempo(prova1)
prova1("ciao")

prova2("ciao ","mondo")

