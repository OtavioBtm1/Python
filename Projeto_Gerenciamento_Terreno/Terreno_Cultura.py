# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132

import datetime

hora = datetime.datetime.now().time()

if hora.hour < 12:
    msg = "Bom dia!"
elif hora.hour < 18:
    msg = "Boa tarde!"
else:
    msg = "Boa noite!"

# Lista de zonas
zonas = {
    1: "Norte",
    2: "Nordeste",
    3: "Sudeste",
    4: "Sul",
    5: "Centro-Oeste"
}

# Dicionário de estados com suas respectivas zonas e terrenos
estados = {
    "Acre": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Acre aqui
        }
    },
    "Alagoas": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Alagoas aqui
        }
    },
    "Amapá": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Amapá aqui
        }
    },
    "Amazonas": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Amazonas aqui
        }
    },
    "Bahia": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para a Bahia aqui
        }
    },
    "Ceará": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Ceará aqui
        }
    },
    "Distrito Federal": {
        "zona": 5,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Distrito Federal aqui
        }
    },
    "Espírito Santo": {
        "zona": 3,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Espírito Santo aqui
        }
    },
    "Goiás": {
        "zona": 5,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Goiás aqui
        }
    },
    "Maranhão": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Maranhão aqui
        }
    },
    "Mato Grosso": {
        "zona": 5,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Mato Grosso aqui
        }
    },
    "Mato Grosso do Sul": {
        "zona": 5,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Mato Grosso do Sul aqui
        }
    },
    "Minas Gerais": {
        "zona": 3,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Minas Gerais aqui
        }
    },
    "Pará": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Pará aqui
        }
    },
    "Paraíba": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para a Paraíba aqui
        }
    },
    "Paraná": {
        "zona": 4,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Paraná aqui
        }
    },
    "Pernambuco": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Pernambuco aqui
        }
    },
    "Piauí": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Piauí aqui
        }
    },
    "Rio de Janeiro": {
        "zona": 3,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Rio de Janeiro aqui
        }
    },
    "Rio Grande do Norte": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Rio Grande do Norte aqui
        }
    },
    "Rio Grande do Sul": {
        "zona": 4,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para o Rio Grande do Sul aqui
        }
    },
    "Rondônia": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Rondônia aqui
        }
    },
    "Roraima": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Roraima aqui
        }
    },
    "Santa Catarina": {
        "zona": 4,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Santa Catarina aqui
        }
    },
    "São Paulo": {
        "zona": 3,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para São Paulo aqui
        }
    },
    "Sergipe": {
        "zona": 2,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Sergipe aqui
        }
    },
    "Tocantins": {
        "zona": 1,
        "terrenos": {
            "Terreno 1": {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            },
            # Adicione outros terrenos para Tocantins aqui
        }
    },
}
culturas = {
    "Milho": {
        "PH do Solo": 6.0,
        "Matéria Orgânica": 2.0,
        "Nível de Nutrientes": 150,
        "Umidade do Solo": 50,
        "Temperatura": 25
    },
    "Feijão": {
        "PH do Solo": 6.5,
        "Matéria Orgânica": 2.5,
        "Nível de Nutrientes": 120,
        "Umidade do Solo": 60,
        "Temperatura": 28
    },
    "Batata": {
        "PH do Solo": 5.5,
        "Matéria Orgânica": 3.0,
        "Nível de Nutrientes": 200,
        "Umidade do Solo": 70,
        "Temperatura": 22
    }
}


def verificar():
    while True:
        print(f"\n  ----{msg}----\nSeja bem-vindo ao sistema de verificação do terreno!")
        for zona, nome in zonas.items():
            print(f"Zona {zona}: {nome}")
        zona_escolhida = input("Você deseja verificar qual zona? Pressione X para sair para o menu: ")
        if zona_escolhida.lower() == 'x':
            print(f"{msg}! Muito Obrigado!!")
            menu()
        elif zona_escolhida.isdigit() and int(zona_escolhida) in zonas:
            zona_escolhida = int(zona_escolhida)
            estados_regiao = [estado for estado, estado_info in estados.items() if estado_info['zona'] == zona_escolhida]
            estados_numerados = {i + 1: estado for i, estado in enumerate(estados_regiao)}
            for i, estado in estados_numerados.items():
                print(f"{i}. {estado}")
            estado_escolhido = input("Qual estado você deseja verificar? (X - Voltar ao menu): ")
            if estado_escolhido.lower() == 'x':
                continue  # Volta ao início do loop para mostrar novamente as opções do menu
            elif estado_escolhido.isdigit() and int(estado_escolhido) in estados_numerados:
                estado_selecionado = estados_numerados[int(estado_escolhido)]
                terrenos_estado = estados[estado_selecionado].get('terrenos', {})
                print(f"Terrenos do estado {estado_selecionado}:\n")
                if terrenos_estado:
                    for terreno, atributos in terrenos_estado.items():
                        print(f"\nInformações do terreno {terreno}:\n")
                        for atributo, valor in atributos.items():
                            print(f"******{atributo}: {valor}******\n")
                else:
                    print("Nenhum terreno encontrado.")
                input("Pressione qualquer tecla para voltar ao menu")
                continue  # Volta ao início do loop para mostrar novamente as opções do menu
            else:
                print("Estado inválido!")
        else:
            print("Zona inválida!")


def valor_terreno():
    print(f"------ {msg}, Seja bem-vindo ao sistema de atribuição de valores aos terrenos! ------")
    
    while True:
        opc = input("Você deseja:\n1- Adicionar valores\n2- Alterar valores\n3- Sair para o menu ")
        
        if opc == '1':
            print("Opção selecionada: Adicionar valores")
            
            for i, zona in zonas.items():
                print(f"{i}. {zona}")
            
            zona_escolhida = int(input("Digite o número da zona: "))
            
            if zona_escolhida in zonas:
                estados_zona = [estado for estado, info in estados.items() if info["zona"] == zona_escolhida]
                
                for i, estado in enumerate(estados_zona, start=1):
                    print(f"{i}. {estado}")
                
                estado_escolhido = int(input("Digite o número do estado: "))
                
                if estado_escolhido in range(1, len(estados_zona) + 1):
                    estado_selecionado = estados_zona[estado_escolhido - 1]
                    
                    terrenos_estado = estados[estado_selecionado].get('terrenos', {})
                    
                    for i, (terreno, atributos) in enumerate(terrenos_estado.items(), start=1):
                        print(f"{i}. {terreno}")
                    
                    terreno_escolhido = int(input("Digite o número do terreno: "))
                    
                    if terreno_escolhido in range(1, len(terrenos_estado) + 1):
                        terreno_selecionado = list(terrenos_estado.keys())[terreno_escolhido - 1]
                        atributos_terreno = terrenos_estado[terreno_selecionado]
                        
                        # Exibir atributos do terreno
                        print(f"\nAtributos do terreno {terreno_selecionado}:\n")
                        for atributo, valor in atributos_terreno.items():
                            print(f"{atributo}: {valor}")
                        
                        # Atualizar os atributos do terreno
                        atributos_terreno["PH do Solo"] = float(input("Digite o valor para PH do Solo: "))
                        atributos_terreno["Matéria Orgânica"] = float(input("Digite o valor para Matéria Orgânica: "))
                        atributos_terreno["Nível de Nutrientes"] = float(input("Digite o valor para Nível de Nutrientes: "))
                        atributos_terreno["Umidade do Solo"] = float(input("Digite o valor para Umidade do Solo: "))
                        atributos_terreno["Temperatura"] = float(input("Digite o valor para Temperatura: "))
                        
                        print("Valores adicionados com sucesso!")
                    else:
                        print("Terreno inválido!")
                else:
                    print("Estado inválido!")
            else:
                print("Zona inválida!")
                
        elif opc == '2':
            print("Opção selecionada: Alterar valores")
            for i, zona in zonas.items():
                print(f"{i}. {zona}")
            
            zona_escolhida = int(input("Digite o número da zona: "))
            
            if zona_escolhida in zonas:
                estados_zona = [estado for estado, info in estados.items() if info["zona"] == zona_escolhida]
                
                for i, estado in enumerate(estados_zona, start=1):
                    print(f"{i}. {estado}")
                
                estado_escolhido = int(input("Digite o número do estado: "))
                
                if estado_escolhido in range(1, len(estados_zona) + 1):
                    estado_selecionado = estados_zona[estado_escolhido - 1]
                    
                    terrenos_estado = estados[estado_selecionado].get('terrenos', {})
                    
                    for i, (terreno, atributos) in enumerate(terrenos_estado.items(), start=1):
                        print(f"{i}. {terreno}")
                    
                    terreno_escolhido = int(input("Digite o número do terreno: "))
                    
                    if terreno_escolhido in range(1, len(terrenos_estado) + 1):
                        terreno_selecionado = list(terrenos_estado.keys())[terreno_escolhido - 1]
                        atributos_terreno = terrenos_estado[terreno_selecionado]
                        
                        # Exibir atributos do terreno
                        print(f"\nAtributos do terreno {terreno_selecionado}:\n")
                        for atributo, valor in atributos_terreno.items():
                            print(f"{atributo}: {valor}")
                        
                        # Atualizar os atributos do terreno
                        atributos_terreno["PH do Solo"] = float(input("Digite o valor para PH do Solo: "))
                        atributos_terreno["Matéria Orgânica"] = float(input("Digite o valor para Matéria Orgânica: "))
                        atributos_terreno["Nível de Nutrientes"] = float(input("Digite o valor para Nível de Nutrientes: "))
                        atributos_terreno["Umidade do Solo"] = float(input("Digite o valor para Umidade do Solo: "))
                        atributos_terreno["Temperatura"] = float(input("Digite o valor para Temperatura: "))
                        
                        print("Valores alterados com sucesso!")
                    else:
                        print("Terreno inválido!")
                else:
                    print("Estado inválido!")
            else:
                print("Zona inválida!")
            
        elif opc == '3':
            print(f"{msg}! Muito Obrigado!!")
            menu()
        
        else:
            print("Opção inválida!")

def adicionar_terreno():
    while True:
        print("\n---- MENU ----")
        print("1. Adicionar terreno")
        print("2. Sair\n")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
        # Solicita a zona geográfica
            print("Zonas:")
            for zona_num, zona_nome in zonas.items():
                print(f"{zona_num}: {zona_nome}")
            zona = int(input("Digite o número da zona geográfica: "))

            # Solicita o estado
            print("\nEstados na zona selecionada:")
            estados_na_zona = [estado for estado, info in estados.items() if info['zona'] == zona]
            for i, estado in enumerate(estados_na_zona, start=1):
                print(f"{i}: {estado}")
            estado_index = int(input("Digite o número correspondente ao estado: "))
            estado_selecionado = estados_na_zona[estado_index - 1]

            # Adiciona o terreno ao estado selecionado
            terreno_nome = input("Digite o nome do terreno: ")
            terreno = {
                "PH do Solo": 0,
                "Matéria Orgânica": 0,
                "Nível de Nutrientes": 0,
                "Umidade do Solo": 0,
                "Temperatura": 0
            }
            estados[estado_selecionado]['terrenos'][terreno_nome] = terreno

            print(f"\nTerreno '{terreno_nome}' adicionado ao estado '{estado_selecionado}'.")
        else:
            menu()
######### Função para verificar os atributos de cada terreno e o quanto falta para chegar em tal cultura  
def verificar_cultura_adequada(atributos):
    for cultura, requisitos in culturas.items():
        atende_requisitos = True
        ajustes_necessarios = []
        for atributo, valor_requerido in requisitos.items():
            if atributo not in atributos or atributos[atributo] < valor_requerido:
                atende_requisitos = False
                ajuste = valor_requerido - atributos.get(atributo, 0)
                ajustes_necessarios.append(f"{atributo}: {ajuste}")
        if atende_requisitos:
            print(f"O terreno atende aos requisitos da cultura: {cultura}")
        else:
            ajustes = ", ".join(ajustes_necessarios)
            print(f"Necessário ajustar os seguintes atributos para o cultivo de {cultura}: {ajustes}")

def cultura():
    print(f"\n  ----{msg}----\nSeja bem-vindo ao sistema de consulta de culturas por terreno!")

    while True:
        for zona, nome in zonas.items():
            print(f"Zona {zona}: {nome}")
        zona_escolhida = input("Você deseja verificar qual zona? Pressione X para sair para o menu: ")
        if zona_escolhida.lower() == 'x':
            print(f"{msg}! Muito Obrigado!!")
            menu()
        elif zona_escolhida.isdigit() and int(zona_escolhida) in zonas:
            zona_escolhida = int(zona_escolhida)
            estados_regiao = [estado for estado, estado_info in estados.items() if estado_info['zona'] == zona_escolhida]
            estados_numerados = {i + 1: estado for i, estado in enumerate(estados_regiao)}
            for i, estado in estados_numerados.items():
                print(f"{i}. {estado}")
            estado_escolhido = input("Qual estado você deseja verificar? (X - Voltar ao menu): ")
            if estado_escolhido.lower() == 'x':
                return  # Retorna à função menu
            elif estado_escolhido.isdigit() and int(estado_escolhido) in estados_numerados:
                estado_selecionado = estados_numerados[int(estado_escolhido)]
                terrenos_estado = estados[estado_selecionado].get('terrenos', {})
                print(f"Terrenos do estado {estado_selecionado}:\n")
                if terrenos_estado:
                    for terreno, atributos in terrenos_estado.items():
                        print(f"\nInformações do terreno {terreno}:\n")
                        for atributo, valor in atributos.items():
                            print(f"******{atributo}: {valor}******\n")
                        # Verificar culturas possíveis com base nos valores dos atributos do terreno
                        culturas_possiveis = []
                        for cultura, requisitos in culturas.items():
                            atende_requisitos = True
                            for atributo, valor_requerido in requisitos.items():
                                if atributo not in atributos or atributos[atributo] < valor_requerido:
                                    atende_requisitos = False
                                    break
                            if atende_requisitos:
                                culturas_possiveis.append(cultura)
                        if culturas_possiveis:
                            print(f"Culturas possíveis no terreno {terreno}:")
                            for cultura in culturas_possiveis:
                                print(f"- {cultura}")
                        else:
                            escolha = input("Deseja verificar o necessário para o resto das culturas?\n1- Sim\n2- Não: ")
                            if escolha == "1":
                                # Verificar o necessário para o resto das culturas
                                print("Necessário ajustar os seguintes atributos para o cultivo de:")

                                for cultura in culturas:
                                    if cultura not in culturas_possiveis:
                                        requisitos = culturas[cultura]
                                        ajustes_necessarios = []
                                        for atributo, valor_requerido in requisitos.items():
                                            ajuste = valor_requerido - atributos.get(atributo, 0)
                                            ajustes_necessarios.append(f"{atributo}: {ajuste}")
                                        ajustes = ", ".join(ajustes_necessarios)
                                        print(f"{cultura}: {ajustes}")
                            elif escolha == "2":
                                print("\nTudo bem!\n")
                                break
                            else:
                                print("Resposta inválida!")

                else:
                    print("Nenhum terreno encontrado.")
            else:
                print("Estado inválido!")
        else:
            print("Zona inválida!")


def adicionar_cultura():
    print("Seja bem-vindo ao adicionar cultura!")
    nome_cultura = input("Digite o nome da nova cultura: ")

    atributos = {}

    ph_solo = float(input("Digite o valor de pH do solo: "))
    atributos["PH do Solo"] = ph_solo

    materia_organica = float(input("Digite o valor de Matéria Orgânica: "))
    atributos["Matéria Orgânica"] = materia_organica

    nivel_nutrientes = int(input("Digite o valor de Nível de Nutrientes: "))
    atributos["Nível de Nutrientes"] = nivel_nutrientes

    umidade_solo = int(input("Digite o valor de Umidade do Solo: "))
    atributos["Umidade do Solo"] = umidade_solo

    temperatura = int(input("Digite o valor de Temperatura: "))
    atributos["Temperatura"] = temperatura

    culturas[nome_cultura] = atributos

    print(f"A cultura '{nome_cultura}' foi adicionada com sucesso!")
    menu()




def consultar_culturas():
    print("Lista de Culturas:")
    for cultura in culturas:
        print(f"Nome da Cultura: {cultura}")
        atributos = culturas[cultura]
        for atributo, valor in atributos.items():
            print(f"{atributo}: {valor}")
        print()
    dec=input("1- Sair para o menu\n2- Mostrar a lista novamente")
    if dec=="1":
        menu()
    elif dec=="2":
        consultar_culturas()
    else:
        print("Opção Inválida")

def menu():
    dec = input(f"------- {msg} -------\nBem-vindo ao menu da TerraIA!!\nPor favor, selecione uma opção:\n1 - Gerenciamento de valores dos terrenos\n2 - Consulta dos valores\n3 - Tipos de culturas por terreno\n4- Adicionar terreno\n5- Adicionar cultura\n6- Consultar culturas\n(Digite qualquer outro caractere para sair)")

    if dec == "1":
        valor_terreno()
    elif dec == "2":
        verificar()
    elif dec == "3":
        cultura()
    elif dec == "4":
        adicionar_terreno()
    elif dec == "5":
        adicionar_cultura()
    elif dec == "6":
        consultar_culturas()
    else:
        print(f"{msg} Muito Obrigado, até mais!")
        exit()

menu()










