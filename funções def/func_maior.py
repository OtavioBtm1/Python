def nummaior():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        mensagem = f"O maior entre os números é {num1}"
    elif num2 > num1:
        mensagem = f"O maior entre os números é {num2}"
    else:
        mensagem = "Os números são iguais"
    return mensagem

resultado = nummaior()
print(resultado)
