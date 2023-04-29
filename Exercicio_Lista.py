# Escreva um programa que preencha uma lista com n números inteiros positivos, 
# digitados pelo usuário. Em seguida, o programa deve exibir a soma dos números ímpares 
# na lista e a média dos números pares na lista. Se a lista estiver vazia ou não contiver 
# nenhum número ímpar ou par, 
# o programa deve exibir uma mensagem apropriada.
tam = 10
lista = []
soma_impares = 0
soma_pares=0

for i in range(tam):
    n = int(input(f"Digite um número para a lista na posição {i}: "))
    lista.append(n)

impares = [n for n in lista if n%2 == 1]
pares = [n for n in lista if n%2==0]

for x in pares:
    soma_pares += x
for x in impares:
    soma_impares += x
print(f"Numeros impares: {impares}")
print(f"Numeros impares somados {soma_impares}")
print(f"Numeros pares:{pares}, somados dão {soma_pares}, media dos pares por {tam} é {soma_pares/tam}")
