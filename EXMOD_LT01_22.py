valor1=0
valor2=0

def recebevalor():
    global valor1, valor2
    valor1=int(input("Digite o primeiro valor: "))
    valor2=int(input("Digite o segundo valor: "))

def crescente():
    if valor1 > valor2:
        print (valor2, valor1)
    elif valor1 == valor2:
        print ("OS NUMEROS NAO PODEM SER IGUAIS")
    else:
        print (valor1, valor2)

def main():
    recebevalor()
    crescente()

if __name__ == "__main__":
    main()
