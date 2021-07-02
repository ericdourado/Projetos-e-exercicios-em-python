'''
Um jogo ABC controla a capacidade de compra de um jogador considerando cada objetivo
alcançado em uma fase, conforme exemplo abaixo. Caso o objetivo não seja atingido, o valor não é
computado para o jogador no momento da compra de itens. Faça um programa que calcule, com
base em uma matriz de entrada, quanto o jogador poderá gastar na próxima compra.
'''

# FASES =                         F1,  F2,   F3,
# OBJETIVO: MATAR OUTROS PLAYERS: 5 ,  10,   15,
# COMPRAS =                       1K  1.5k   4K

# Itens para comprar =  [espada, arco, escudo.]
#                       [2000    1000   500   ]

fases = ['Fase1','Fase2','Fase3']
objetivo_do_jogo = [5,10,15]
dinheiro_FASE = [1000,1500,2000]
itens_para_comprar =  ['espada', 'arco', 'escudo']
valor_de_cada_item = [2000, 1500, 500]
acumulador_em_cada_fase = []
dinheiro_acumulado = 0
mochila_do_jogador = []
quantidade_de_kills = []

# INTRODUÇÃO
print('Opa meu jogador, seja bem vindo, a seguir te mostraremos a quantidade de fases e o objetivo delas...'
      'Caso nao atinja o objetivo, você nao ganhará a recompensa\n\n')


for x in range(0, len(fases)):
    print(fases[x],'=' ,' Matar' ,objetivo_do_jogo[x],'jogadores',' Voce ganhará:',dinheiro_FASE[x],'moedas ')

print('\n\nFASE 1 VAMOS LÁ!!!\n')
# FASE 1
objetivo_fase = int(input('\n Quantos jogadores voce matou nesta fase jogador? '))
if objetivo_fase >= objetivo_do_jogo[0]:
    dinheiro_acumulado += dinheiro_FASE[0]
    acumulador_em_cada_fase.append(dinheiro_FASE[0])
    print(f' parabens meu jogador, você atingiu o objetivo da Desta FASE, portanto você vc tem na bolsa R${dinheiro_acumulado}')
    print()
    quantidade_de_kills.append(objetivo_fase)
else:
    acumulador_em_cada_fase.append(0)
    quantidade_de_kills.append(objetivo_fase)
    print('Voce matou muito pouco, portanto nao atingiu seu objetivo')
    print()


# FASE - ACESSO A LOJA
def perguntas():
    global dinheiro_acumulado
    while True:
        pergunta1 = int(input('Deseja acessar a loja antes de ir para a Próxima fase? 1 - Sim e 2 - Nao: \n'))
        if pergunta1 == 1:
            print('Deseja comprar algo? 1 - espada, 2 - arco, 3- escudo')
            for itens in range(0,len(itens_para_comprar)):
                print(f'{itens_para_comprar[itens]} = R${valor_de_cada_item[itens]}')
            item_escolhido = int(input('\n Digite o numero do item aqui: '))

            if item_escolhido == 1:
                if dinheiro_acumulado < valor_de_cada_item[0]:
                    print('voce nao tem dinheiro suficiente, escolha outro item')
                    continue
                else:
                    print(f'OK {itens_para_comprar[0]} comprado!!! e ja está na sua bolsa.')
                    mochila_do_jogador.append('espada')
                    dinheiro_acumulado = dinheiro_acumulado - valor_de_cada_item[0]
                    return dinheiro_acumulado


            if item_escolhido == 2:
                if dinheiro_acumulado < valor_de_cada_item[1]:
                    print()
                    print('voce nao tem dinheiro suficiente, escolha outro item')
                    print()
                    continue
                else:
                    print(f'OK {itens_para_comprar[1]} comprado!!! e ja está na sua bolsa.')
                    mochila_do_jogador.append('arco')
                    dinheiro_acumulado = dinheiro_acumulado - valor_de_cada_item[1]
                    return dinheiro_acumulado


            if item_escolhido == 3:
                if dinheiro_acumulado < valor_de_cada_item[2]:
                    print()
                    print('voce nao tem dinheiro suficiente, escolha outro item:')
                    print()
                    continue
                else:
                    print(f'OK {itens_para_comprar[2]} comprado!!! e ja está na sua bolsa.')
                    mochila_do_jogador.append('escudo')
                    dinheiro_acumulado = dinheiro_acumulado - valor_de_cada_item[2]
                    return dinheiro_acumulado
        else:
            break

perguntas()

# FASE 2
print(f'Você tem agora R${dinheiro_acumulado}\n')
print('\n OK ENTÃO IREMOS PARA A FASE 2 \n')


objetivo_fase = int(input('Quantos jogadores voce matou nesta fase jogador? '))
if objetivo_fase >= objetivo_do_jogo[1]:
    acumulador_em_cada_fase.append(dinheiro_FASE[1])
    dinheiro_acumulado += dinheiro_FASE[1]
    quantidade_de_kills.append(objetivo_fase)
    print(f' parabens meu jogador, você atingiu o objetivo da Desta FASE, portanto você vc tem na bolsa R${dinheiro_acumulado}')
    print()
else:
    acumulador_em_cada_fase.append(0)
    quantidade_de_kills.append(objetivo_fase)
    print('Voce matou muito pouco, portanto nao atingiu seu objetivo')
    print()

perguntas()
print(f'Você tem agora R${dinheiro_acumulado}\n')


#FASE 3
print('OK ENTÃO IREMOS PARA A FASE 3 \n')

objetivo_fase = int(input('Quantos jogadores voce matou nesta fase jogador? '))
if objetivo_fase >= objetivo_do_jogo[2]:
    acumulador_em_cada_fase.append(dinheiro_FASE[2])
    dinheiro_acumulado += dinheiro_FASE[2]
    quantidade_de_kills.append(objetivo_fase)
    print(f' parabens meu jogador, você atingiu o objetivo da desta FASE, portanto você vc tem na bolsa R${dinheiro_acumulado}')
    print()
else:
    acumulador_em_cada_fase.append(0)
    quantidade_de_kills.append(objetivo_fase)
    print('Voce matou muito pouco, portanto nao atingiu seu objetivo')
    print()

perguntas()

print('\nFIM DE JOGO!!!!!\n')

# FINAL DE GAME #
print(f'Voce finalizou o jogo com:')
for itens in range(0, len(fases)):
    print(f'{fases[itens]} = voce matou {quantidade_de_kills[itens]} e acumulou {acumulador_em_cada_fase[itens]}')

for mochila in mochila_do_jogador:
    print(f'Itens na sua mochila: {mochila}')
print(f'Dinheiro acumulado R${dinheiro_acumulado}')