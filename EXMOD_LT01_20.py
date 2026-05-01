import math

a=0
b=0
c=0
delta=0
x1=0
x2=0

def recebevalores():
    a=float(input("Digite o valor A: "))
    b=float(input("Digite o valor B: "))
    c=float(input("Digite o valor C: "))

def calculo():
    global a, b, c, delta, x1, x2
    delta = ((b * b) - 4 * a * c )
    if (delta > 0):
        x1 = (-b + (math.sqrt(delta)) / (2*a))
        x2 = (-b - (math.sqrt(delta)) / (2*a))
        print ("A primeira raiz é: ",x1)
        print ("A segunda raiz é: ",x2)
    else:
        print ("Não tem raizes reais.")

def main():
    recebevalores()
    calculo()
if __name__ == "__main__":
    main()
