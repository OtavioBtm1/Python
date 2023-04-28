cont = int(input("Digite o valor do contador: "))
lista = []
for i in range(cont):
    x = int(input(f"Digite o valor numero {i} para a lista: "))
    lista.append(x)
pares=[x for x in lista if x%2==0]
print(lista)
print(pares)
