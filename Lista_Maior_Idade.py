qtd = int(input("Digite a quantidade de pessoas: "))
pessoas = []
b = 0

for i in range(qtd):
    idade = int(input("Digite a sua idade: "))
    pessoas.append(idade)

menor = [idade for idade in pessoas if idade < 18]

for idade in menor:
    b += 1

print(f"Existem {b} menores de 18 anos na lista.")