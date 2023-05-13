import math

def modulo():
    while True:
        num1 = float(input("Digite um número negativo para obter o seu módulo: "))
        if num1 < 0:
            num1 = num1**2 # Calcula o valor absoluto do número negativo
            raiz = math.sqrt(num1)
            return raiz
        else:
            print("Digite um número negativo!")
resultado = modulo()
print(f"O módulo do número é {resultado}")


