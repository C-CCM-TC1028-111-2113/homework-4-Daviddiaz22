
def main():
    #Escribe tu código debajo de esta línea
    n = int(input('Enter triangle height: '))
    a=1
    sp= n - 1

    for i in range(a,n+1,1):
        print((' '* sp)+'*' * i)
        sp = sp - 1

if __name__=='__main__':
    main()
