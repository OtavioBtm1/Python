def calcular_fatorial():
    numero = int(input("Digite um número para calcular o seu fatorial: "))
    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    return fatorial

resultado = calcular_fatorial()
print(f"O fatorial é {resultado}")
