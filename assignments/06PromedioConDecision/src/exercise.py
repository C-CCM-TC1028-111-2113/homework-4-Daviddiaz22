def main():
    #escribe tu código abajo de esta línea
    i = 0
    sum = 0

    while True:
        num =float(input())
        if num >= 0:
            i = i + 1
            sum = sum + num
        else:
            print(str(sum/i))
            break
if __name__=='__main__':
    main()
