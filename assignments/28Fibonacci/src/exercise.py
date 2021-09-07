
def main():
    #escribe tu código abajo de esta línea
    indi = int(input('Enter the index: '))
    i = 1
    front = 1   
    back = 0
    supp = 0

    while i <= indi:
        supp = front
        front = front + back
        back = supp 
        i += 1
    print(back) 

if __name__=='__main__':
    main()
