

def main():
    #Escribe tu código debajo de esta línea
    num = int(input('Escribe un numero : '))
    i = 1

    while i**2 <= num:
        i = i + 1
    print(i)

if __name__=='__main__':
    main()
