valor1=0
valor2=0
valor3=0
valor4=0

def valores():
    global valor1, valor2, valor3, valor4
    valor1=int(input("Digite o primeiro valor: "))
    valor2=int(input("Digite o segundo valor: "))
    valor3=int(input("Digite o terceiro valor: "))
    valor4=int(input("Digite o quarto valor: "))

    valores = [valor1, valor2, valor3, valor4]
    valores.sort()
    print(valores)


def main():
  valores()

if __name__ == "__main__":
    main()
