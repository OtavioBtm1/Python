def par():
    num1=int(input("Digite um numero para saber se é par: "))
    if num1 % 2 == 0:
        res= "O numero é par"
    else:
        res= "O numero é impar"
    return res
print(par())