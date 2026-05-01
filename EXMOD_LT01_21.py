nota1=0
nota2=0
nota3=0
nota4=0
media=0

def recebenotas():
    global nota1, nota2, nota3, nota4, media
    nota1=float(input("Digite a nota do primeiro bimestre: "))
    nota2=float(input("Digite a nota do segundo bimestre: "))
    nota3=float(input("Digite a nota do terceiro bimestre: "))
    nota4=float(input("Digite a nota do quarto bimestre: "))

def calculomedia():
    media = ((nota1 + nota2 + nota3 + nota4) / 4)
    if (media >= 6.0):
        print ("Aprovado!")
    elif (media >= 3.0) and (media < 6.0):
        print ("Recuperação")
    else:
        print ("Retido!")
def main():
    recebenotas()
    calculomedia()
    
if __name__ == "__main__":
    main()
