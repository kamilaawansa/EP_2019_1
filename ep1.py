# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Kamila Addel Wansa, kamilaaw@al.insper.edu.br
# - aluno B: Maria Victoria Cavalieri, mariavpcc@insper.edu.br  
from random import randint   
def carregar_cenarios():
    cenarios = {
        "Opções combate": {
            "titulo": "COMBATE",
            "descricao": "Você entrou em um combate",
            "opcoes": {
                "decisao1": "Abraçar o panda da sala mágica",
                "decisao2": "Chutar o panda da sala mágica"
            }
        },
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    inventario=[]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual["titulo"])
        print("-"* len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print()
        
        opcoes = cenario_atual["opcoes"]
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Escolha sua opção: ")
            print()
            for opcao,valor in opcoes.items():
                print('{0}:{1}'.format(opcao,valor))
                
            escolha = input("O que você quer fazer? ") 
                
            if escolha in opcoes:
                nome_cenario_atual = escolha
                #hit point: FEATURE 1 
                MP=(["MONSTRO!!!", "PRÊMIO"][randint(0,1)])
                print(MP)
                if MP== "MONSTRO!!!":
                    #FEATURE 2 
                    print("COMBATE!")
                    print()
                    print["Opções combate"]
                    print("Escolha sua opção: ")
                    decisao1= "Atacar monstro com um garfo"
                    print(decisao1)
                    decisao2= "Atacar monstro com espada"
                    print(decisao2)
                    print()
                    decisao=input("O que você vai fazer? ")
                    if decisao==decisao1:
                        game_over = True 
                    else: 
                        print("Você derrotou o monstro!")
                        print()
                        print('Você ganhou uma chave')
                        inventario.append('chave')
                        print(inventario)
                        print()
                elif MP== "PRÊMIO":
                    print("Você ganhou 100 moedas de ouro!")
                    inventario.append('100 moedas de ouro')
                    print(inventario)
                    print()
                    print('Você ganhou uma chave')
                    inventario.append('chave')
                    print(inventario)
                    print()
                if 'chave' in inventario:
                    print(' você entrou na sala mágica com a sua chave!!')
                    print('Escolha sua opção:  ')
                    decisao1= "Abraçar o panda da sala mágica"
                    print(decisao1)
                    decisao2= "Chutar o panda da sala mágica"
                    print(decisao2)
                    print()
                    decisao=input("O que você vai fazer? ")
                    if decisao==decisao1:
                        print('parabéns, você ganhou um prêmio!')
                        PR=(["moedas de ouro", "poção mágica"][randint(0,1)])
                        print(PR) 
                    if PR== "moedas de ouro":
                        print('parabéns, você ganhou moedas!!!')
                        inventario.append('20 moedas')
                        print(inventario)
                    elif PR== "poção mágica":
                        print('parabéns, você ganhou uma poção mágica!')
                        inventario.append('poção mágica')  
                        print(inventario)
                    if decisao==decisao2:
                        print('O panda se irritou com você!')
                #Feature 4 (teletransporte)
                ativar_tel= randint(1,10)
                if len(opcoes)==0:
                    print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                    game_over= True
                elif ativar_tel==2:
                    cenario_desejado= input('Parabéns, você tem direito a um teletransporte! Para qual cenário você quer ir? ')
                    if cenario_desejado in cenarios:
                        nome_cenario_atual= cenario_desejado
                    else:
                        print('Esse não é um cenário possível!')
                        game_over=True 
                    break
    else:
            print("Sua indecisão foi sua ruína!")
            game_over = True
    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()
         