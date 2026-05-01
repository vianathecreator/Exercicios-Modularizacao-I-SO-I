valor=0

def numdivisivel():
    global valor
    valor=int(input("Digite um valor inteiro: "))
    if valor % 2 == 0:
        print ("Numero é divisivel por 2")
    else: 
        print ("Numero não é divisivel por 2")

    if valor % 3 == 0:
        print ("Numero é divisivel por 3")
    else:
        print ("Numero nao é divisivel por 3")

def main():
    numdivisivel()

if __name__ == "__main__":
    main()
