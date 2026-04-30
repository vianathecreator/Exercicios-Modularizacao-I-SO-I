valor1 = 0
valor2 = 0
resultado = 0

def diferençavalores():
    global  valor1, valor2, resultado

    valor1 = int(input("Digite o valor 1: "))
    valor2 = int(input("Digite o valor 2: "))

    resultado = valor1 - valor2

def main():
    diferençavalores()
    print ("A diferença entre os valores é de:", resultado)

if __name__ == "__main__":
    main()
