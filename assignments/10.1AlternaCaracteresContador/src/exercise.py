def main():
    #escribe tu código abajo de esta línea
    b = int(input('ingresa un numero'))
    a = 1

    for i in range(a,b+1,1):
        if i%2 == 0:
            print(str(i)+"-%")
        else:
            print(str(i)+"-#")

if __name__=='__main__':   
    main()
