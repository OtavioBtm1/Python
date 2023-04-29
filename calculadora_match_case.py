while True:
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    operador = input("Digite o operador (+, -, *, /): ")

    resultado = 0
    operacao_valida = True

    match operador:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            if num2 == 0:
                print("Não é possível dividir por zero")
                operacao_valida = False
            else:
                resultado = num1 / num2
        case _:
            print("Operador inválido, digite um certo")
            operacao_valida = False

    if operacao_valida:
        print(f"Resultado: {resultado}")
        break

