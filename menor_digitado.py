tam = 5
num = []
n = float('inf')

for i in range(tam):
    numeros = int(input("Digite os numeros: "))
    num.append(numeros)
    if numeros < n:
        n = numeros

print(n)
