import datetime

# Classe Pessoa para representar as informações de cada pessoa
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.consumo_agua =0
        self.descargas=0

    def saudacao(self):
        hora_atual = datetime.datetime.now().time()
        if hora_atual.hour >= 6 and hora_atual.hour < 12:
            return 'Bom dia'
        elif hora_atual.hour >= 12 and hora_atual.hour < 18:
            return 'Boa tarde'
        elif hora_atual.hour >= 18 and hora_atual.hour < 24:
            return 'Boa noite'

positivo = ['s', 'S', 'Sim', 'SIM', 'sim', 'ss', 'SS']
negativo = ['n', 'N', 'Não', 'Nao', 'nao', 'nn', 'Nn', 'NAO', 'NÃO']

pessoas = []

def menu():
    saud = Pessoa.saudacao(Pessoa)
    print(f"Olá, {saud}")
    
    while True:
        try:
            dec = int(input('1- Já possuo cadastro!\n2- Quero me cadastrar!\n3- Sair\n'))
            if dec in [1, 2, 3]:
                break
            else:
                print('Opção inválida. Escolha 1, 2 ou 3.')
        except ValueError:
            print('Opção inválida. Digite um número válido.')

    if dec == 1:
        while True:
            busca_nome = input("Qual é o seu nome?")
            encontrado = False

            for pessoa in pessoas:
                if pessoa.nome.lower() == busca_nome.lower():
                    print(f'Bem-vindo de volta, {pessoa.nome}!')
                    menu_pessoa(pessoa)
                    encontrado = True
                    break

            if not encontrado:
                print(f'Pessoa com nome "{busca_nome}" não encontrada.')
                input("Pressione enter para retornar!\n")
                menu()
    elif dec == 2:
        print("Vamos para o cadastro!")
        cadastro()
    elif dec == 3:
        print("Até mais!")
        exit()
    else:
        menu()


def cadastro():
    saud = Pessoa.saudacao(Pessoa)  # Obtém a saudação usando a classe Pessoa
    print(f'Olá, {saud}\nVamos fazer seu cadastro!')
    
    while True:
        nome = input('Qual é o seu nome? ')
        if nome.isalpha():
            break
        else:
            print('Nome inválido. Por favor, digite seu nome.')

    while True:
        try:
            idade = int(input('Qual é a sua idade? '))
            if idade >= 0:
                break
            else:
                print('Idade inválida. A idade deve ser um número positivo ou igual a zero.')
        except ValueError:
            print('Idade inválida. Digite um número válido.')

    while True:
        sexo = input('Qual é o seu sexo? [M/F] ').upper().strip()[0]
        if sexo in 'MF':
            break
        else:
            print('Sexo inválido. Digite M ou F.')

    # Cria um objeto Pessoa e adiciona à lista pessoas
    pessoa = Pessoa(nome, idade, sexo)
    pessoas.append(pessoa)
    print(f'Cadastro realizado com sucesso, {nome}!')
    menu_pessoa(pessoa)


def menu_pessoa(pessoa):
    while True:
        print(f'\nMenu de {pessoa.nome}:')
        print("1. Ver informações pessoais")
        print("2. Sair")
        print("3. Dados")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f'\nInformações de {pessoa.nome}:')
            print(f'Nome: {pessoa.nome}')
            print(f'Idade: {pessoa.idade}')
            print(f'Sexo: {pessoa.sexo}')
            print(f'Consumo de agua: {pessoa.consumo_agua}')
            print(f'Quantidade de descargas: {pessoa.descargas}')
            input("Pressione enter para continuar")
        elif escolha == "2":
            menu()
        elif escolha == "3":
            menu_arduino(pessoa)
        else:
            print("Opção inválida. Tente novamente.")

def menu_arduino(pessoa):
    print("Seja bem-vindo ao menu de dados do Arduino")
    dec = input("Você deseja:\n1- Cadastrar consumo de água ou descargas\n2- Verificar dados de consumo e descargas\n")
    
    while dec not in ["1", "2"]:
        dec = input("Opção inválida. Escolha 1 ou 2: ")

    if dec == "1":
        print("1. Cadastrar consumo de água")
        print("2. Cadastrar quantidade de descargas")
        print("3. Sair para o perfil")
        escolha = input("Escolha uma opção: ")

        while escolha not in ["1", "2", "3"]:
            escolha = input("Opção inválida. Escolha 1, 2 ou 3: ")

        if escolha == "1":
            while True:
                consumo_agua = input("Digite o consumo de água: ")
                if consumo_agua.replace(".", "", 1).isdigit():  # Verifica se a entrada é um número (pode conter um único ponto decimal)
                    pessoa.consumo_agua = float(consumo_agua)
                    break
                else:
                    print("Por favor, digite um valor numérico para o consumo de água.")

        elif escolha == "2":
            while True:
                quantidade_descargas = input("Digite a quantidade de descargas: ")
                if quantidade_descargas.isdigit():  # Verifica se a entrada é um número inteiro
                    pessoa.descargas = int(quantidade_descargas)
                    break
                else:
                    print("Por favor, digite um valor numérico inteiro para a quantidade de descargas.")

        elif escolha == "3":
            print('Obrigado!')
            menu_pessoa(pessoa)

    elif dec == "2":
        print(f'\nInformações de {pessoa.nome}:')
        print(f"Consumo de agua: {pessoa.consumo_agua}")
        print(f"Quantidade de descargas: {pessoa.descargas}")


menu()

    


