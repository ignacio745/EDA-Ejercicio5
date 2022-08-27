from Pila import Pila



if __name__ == "__main__":
    pilas:list[Pila] = []

    numero = int(input("Ingrese el numero de discos: "))

    for i in range(3):
        pilas.append(Pila(int, numero))


    cadena = ""

    for i in range(numero):
        cadena += "{0:^5}{1:^5}{2:^5}\n".format(i+1, "|", "|")
        pilas[0].apilar(numero-i)
    
    cadena += "{0:^5}{1:^5}{2:^5}\n".format("---", "---", "---")
    print(cadena)
    
    movimientos = 0
    
    while not (pilas[0].vacia() and pilas[1].vacia()):
        #print(mostrarTorres(pilas))
        t1 = int(input("Ingrese la torre cuyo disco superior quiere mover: "))
        while not 1<=t1<=3:
            t1 = int(input("Pila invalida, reintente: "))
        
        try:
            d = int(pilas[t1-1].desapilar())
        except Exception:
            print("No hay mas discos en la torre {0}".format(t1))
        else:
            t2 = int(input("Ingrese la torre en la que quiere apilar el disco: "))
            while not (1<=t2<=3 and t2!=t1):
                t2 = int(input("Torre invalida, reintente: "))
            try:
                pilas[t2-1].apilar(d)
            except:
                print("[ERROR] No puede apilar el disco {0} en la torre {1}".format(d, t2))
                pilas[t1-1].apilar(d)
            else:
                print("Se apilo el disco {0} en la pila {1}".format(d, t2))
                movimientos += 1
    
    print("Felicitaciones, gano el juego en {0} movimientos, numero minimo de movimientos posible: {1}".format(movimientos, 2**numero-1))
