valor1 = 0
valor2 = 0

def recebevalores():
    global  valor1, valor2
    valor1 = int(input("Digite o valor 1: "))
    valor2 = int(input("Digite o valor 2: "))

def main():
    recebevalores()
    if (valor1 > valor2):
        print ("O primeiro valor é o maior")
    else:
        print ("O segundo valor é o maior")

if __name__ == "__main__":
    main()
