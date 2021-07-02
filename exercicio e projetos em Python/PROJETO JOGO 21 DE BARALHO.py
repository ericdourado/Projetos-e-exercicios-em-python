'''
3.6 – O Jogo do 21 é um jogo de cartas em que o objetivo é obter a soma de 21 pontos com as
cartas, na sua vez de jogar. Este código possui somente 2 jogadores, porém um código bem complexo,
pois possui as seguintes regras:

1. cada jogador recebe 3 cartas;
2. o primeiro jogador “compra” um carta e descarta uma carta;
3. o próximo jogador pode escolher pegar a carta descartada ou comprar do monte;
4. repete-se os passos 2 e 3 até um dos jogadores alcançar 21 pontos.

Um exemplo de código onde mostra a gerencia de cartas, distribuição, exlusão de cartas do baralho etc.

'''
from random import choice


# Será definido quantos jogadores irão jogar e a quantidade de jogadores será a quantidade de listas criadas

print('             SEJA BEM VINDO, ESTE JOGO É CHAMADO DE 21, ENTRE 2 JOGADORES!!')

jogador_1 = list()
jogador_2 = list()

baralho = [
    {'as de copas': 1, '2 de copas': 2, '3 de copas': 3, '4 de copas': 4, '5 de copas': 5, '6 de copas': 6,
     '7 de copas': 7, '8 de copas': 8, '9 de copas': 9, '10 de copas': 10,
     'Rei de copas': 10, 'Dama de copas': 10, 'Valete de copas': 10},
    {'as de espadas': 1, '2 de espadas': 2, '3 de espadas': 3, '4 de espadas': 4, '5 de espadas': 5, '6 de espadas': 6,
     '7 de espadas': 7, '8 de espadas': 8, '9 de espadas': 9, '10 de espadas': 10,
     'Rei de espadas': 10, 'Dama de espadas': 10, 'Valete de espadas': 10},
    {'as de ouro': 1, '2 de ouro': 2, '3 de ouro': 3, '4 de ouro': 4, '5 de ouro': 5, '6 de ouro': 6, '7 de ouro': 7,
     '8 de ouro': 8, '9 de ouro': 9, '10 de ouro': 10,
     'Rei de ouro': 10, 'Dama de ouro': 10, 'Valete de ouro': 10},
    {'as de paus': 1, '2 de paus': 2, '3 de paus': 3, '4 de paus': 4, '5 de paus': 5, '6 de paus': 6, '7 de paus': 7,
     '8 de paus': 8, '9 de paus': 9, '10 de paus': 10,
     'Rei de paus': 10, 'Dama de paus': 10, 'Valete de paus': 10}
]

x = []  # Desempacotamento PARA SORTEIO DE CARTAS #KEYS STRING
cartasDescartadasJogador1 = []
cartasDescartadasJogador2 = []
somaJogador_1 = 0
somaJogador_2 = 0

# DESEMPACOTAR AS KEYS DO DICIONÁRIO BARALHO PARA DENTRO DE x
for c in baralho:
    for k, v in c.items():
        x.append(f'{k}')
'''
------------------------FUNÇÕES-------------------------
'''


# CONDIÇÕES PARA O JOGADOR GANHAR
def CondicoesDeVitoria():
    global true
    global true1
    if somaJogador_1 == 21:
        print('Parabéns o jogador 1 venceu!!')
        true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true != 1:
            true = 0
    elif somaJogador_1 > 21 and somaJogador_2 > 21:
        if somaJogador_1 < somaJogador_2:
            print('O jogador 1 está mais proximo de 21 e venceu o jogo!!')
            true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true != 1:
                true = 0
        else:
            print('O jogador 2 está mais proximo de 21 e venceu o jogo!!')
            true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true != 1:
                true = 0
        if somaJogador_1 == somaJogador_2:
            print('Os 2 jogadores estão empatados')
            true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true != 1:
                true = 0

    elif somaJogador_1 > 21:
        print('O jogador 1 passou de 21, e perdeu o jogo!!!')
        true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true != 1:
            true = 0
    elif somaJogador_2 == 21:
        print('Parabéns o jogador 2 venceu!!')
        true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true != 1:
            true = 0
    elif somaJogador_2 > 21:
        print('O jogador 2 passou de 21, e perdeu o jogo!!!')
        true = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true != 1:
            true = 0

def CondicoesDeVitoria2():
    global true
    global true1
    if somaJogador_1 == 21:
        print('Parabéns o jogador 1 venceu!!')
        true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true1 != 1:
            true1 = 0
    elif somaJogador_1 > 21 and somaJogador_2 > 21:
        if somaJogador_1 < somaJogador_2:
            print('O jogador 1 está mais proximo de 21 e venceu o jogo!!')
            true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true1 != 1:
                true1 = 0
        else:
            print('O jogador 2 está mais proximo de 21 e venceu o jogo!!')
            true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true1 != 1:
                true1 = 0

        if somaJogador_1 == somaJogador_2:
            print('Os 2 jogadores estão empatados')
            true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
            if true1 != 1:
                true1 = 0

    elif somaJogador_1 > 21:
        print('O jogador 1 passou de 21, e perdeu o jogo!!!')
        true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true1 != 1:
            true1 = 0
    elif somaJogador_2 == 21:
        print('Parabéns o jogador 2 venceu!!')
        true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true1 != 1:
            true1 = 0
    elif somaJogador_2 > 21:
        print('O jogador 2 passou de 21, e perdeu o jogo!!!')
        true1 = int(input('Digite 0 para parar o jogo ou 1 para continuar:'))
        if true1 != 1:
            true1 = 0


# REMOVER AS CARTAS DO BARALHO 'x' QUE ESTÃO NAS MAOS DOS JOGADORES
def deleta(player):
    for contador in range(0, len(baralho)):
        for k, v in baralho[contador].items():
            if k in player:
                if k not in x:
                    continue
                x.remove(k)


def mostraCartas(player):
    if player == jogador_1:
        print('CARTAS DO JOGADOR 1')
    else:
        print('CARTAS DO JOGADOR 2')
    for cartas in player:
        print(f'     -{cartas} ')


# SOMAR PONTOS NA MAO DO JOGADOR 1
def somadorDePontosJogador1():
    global somaJogador_1
    global somaJogador_2
    somaJogador_1 = 0
    for contador_2 in baralho:
        for keys, values in contador_2.items():
            for verificarKeys in jogador_1:
                if verificarKeys in keys:
                    somaJogador_1 += values
    print(f'    A soma das cartas do jogador 1 é {somaJogador_1}')


# SOMAR PONTOS NA MAO DO JOGADOR 2
def somadorDePontosJogador2():
    global somaJogador_1
    global somaJogador_2
    somaJogador_2 = 0
    for contador_2 in baralho:
        for keys, values in contador_2.items():
            for verificarKeys in jogador_2:
                if verificarKeys in keys:
                    somaJogador_2 += values
    print(f'    A soma das cartas do jogador 2 é {somaJogador_2}')


# Comprar cartas do baralho e descarta uma;
def compraDescartaJogador(jogador, cartasDescartadas, posicao):
    cartasDescartadas.append(jogador[posicao])
    del jogador[posicao]
    jogador.append(choice(x))


def pegarUltimaCartaDescartada(jogador, cartasDescartadaDoJogadorOposto, cartaEscolhida, posicao):
    del jogador[cartaEscolhida]
    jogador.append(cartasDescartadaDoJogadorOposto[posicao])
    del cartasDescartadaDoJogadorOposto[posicao]


for cartasJogadores1 in range(0, 3):
    jogador_1.append(choice(x))
    deleta(jogador_1)

# Mostrar cartas do jogador:
mostraCartas(jogador_1)
print('*' * 90)

# Remover a carta do baralho caso o jogador tenha na mão
for cartasJogadores2 in range(0, 3):
    jogador_2.append(choice(x))
    deleta(jogador_2)

# Mostrar cartas do jogador 2
mostraCartas(jogador_2)

print(f'                BARALHO ======== {x}')
print('*' * 90)
somadorDePontosJogador1()
somadorDePontosJogador2()
print('*' * 90)

'''
----------------------------------------------------COMANDOS----------------------------------------------------
'''

true = 1
while true == 1:
    CondicoesDeVitoria()
    if true != 1:
        continue
    print('*' * 90)
    # perguntas para o jogador 1
    print('     VEZ DO JOGADOR 1')
    print(
        '\nvoce pode descartar uma carta e comprar uma, não fazer nada ou descartar uma carta e pegar a ultima carta descartada do outro jogador. DIGITE APENA OS NUMEROS')
    mostraCartas(jogador_1)
    compraCarta = int(input(
        'Digite 2 - para descartar uma carta e comprar outra do baralho\nDigite 1 - para não fazer nada\nDigite 0 - Para descartar uma carta e pegar outra carta descartada do jogador 2\n: '))
    if compraCarta == 2:
        print('*' * 90)
        mostraCartas(jogador_1)
        cartasDescartadasExtenso = int(input((
                                                 f'Digite 0 - para descartar a carta {jogador_1[0]}\nDigite 1 - para descartar a carta {jogador_1[1]}\nDigite 2 - para descartar a carta {jogador_1[2]} \n:')))
        if cartasDescartadasExtenso == 0:
            compraDescartaJogador(jogador_1, cartasDescartadasJogador1, 0)
            mostraCartas(jogador_1)
            deleta(jogador_1)
            somadorDePontosJogador1()

        elif cartasDescartadasExtenso == 1:
            compraDescartaJogador(jogador_1, cartasDescartadasJogador1, 1)
            deleta(jogador_1)
            mostraCartas(jogador_1)
            somadorDePontosJogador1()

        elif cartasDescartadasExtenso == 2:
            compraDescartaJogador(jogador_1, cartasDescartadasJogador1, 2)
            deleta(jogador_1)
            mostraCartas(jogador_1)
            somadorDePontosJogador1()

    elif compraCarta == 0:
        if len(cartasDescartadasJogador2) < 1:
            print('\n\t\tO outro jogador não descartou nenhuma carta'.upper())
            continue
        elif len(cartasDescartadasJogador2) >= 1:
            cartasDescartadasExtenso = int(input(
                f'Digite 0 - para descartar a carta {jogador_1[0]}\nDigite 1 - para descartar a carta {jogador_1[1]}\nDigite 2 - para descartar a carta {jogador_1[2]} \n:'))
            if cartasDescartadasExtenso == 0:
                deleta(jogador_1)
                pegarUltimaCartaDescartada(jogador_1, cartasDescartadasJogador2, 0, -1)
                mostraCartas(jogador_1)
                somadorDePontosJogador1()

            elif cartasDescartadasExtenso == 1:
                deleta(jogador_1)
                pegarUltimaCartaDescartada(jogador_1, cartasDescartadasJogador2, 1, -1)
                mostraCartas(jogador_1)
                somadorDePontosJogador1()

            elif cartasDescartadasExtenso == 2:
                deleta(jogador_1)
                pegarUltimaCartaDescartada(jogador_1, cartasDescartadasJogador2, 2, -1)
                mostraCartas(jogador_1)
                somadorDePontosJogador1()

    # -------------------------------- Vez do jogador 2 CONDICIONAL(CASO O JOGADOR 1 DECIDA NAO FAZER NADA) ----------------------------

    elif compraCarta == 1:
        print('         OK VEZ DO JOGADOR 2')
        print(
            'Voce pode descartar uma carta e comprar uma, não fazer nada ou descartar uma carta epegar a ultima carta descartada do outro jogador. DIGITE APENA OS NUMEROS! \n')
        mostraCartas(jogador_2)
        compraCartaJogador2 = int(input(
            'Digite 2 - para descartar uma carta e comprar outra do baralho\nDigite 1 - para não fazer nada\nDigite 0 - Para descartar uma carta e pegar outra carta descartada do jogador 1\n: '))
        if compraCartaJogador2 == 2:
            print('*' * 90)
            mostraCartas(jogador_2)
            cartasDescartadasExtenso2 = int(input(
                f'Digite 0 - para descartar a carta {jogador_2[0]}\nDigite 1 - para descartar a carta {jogador_2[1]}\nDigite 2 - para descartar a carta {jogador_2[2]} \n:'))
            if cartasDescartadasExtenso2 == 0:
                compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 0)
                mostraCartas(jogador_2)
                deleta(jogador_2)
                somadorDePontosJogador2()
                CondicoesDeVitoria()
                if true != 1:
                    continue
                continue

            elif cartasDescartadasExtenso2 == 1:
                compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 1)
                deleta(jogador_2)
                mostraCartas(jogador_2)
                somadorDePontosJogador2()
                CondicoesDeVitoria()
                if true != 1:
                    continue
                continue

            elif cartasDescartadasExtenso2 == 2:
                compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 2)
                deleta(jogador_2)
                mostraCartas(jogador_2)
                somadorDePontosJogador2()
                CondicoesDeVitoria()
                if true != 1:
                    continue
                continue

        elif compraCartaJogador2 == 1:
            print('     OK VEZ DO JOGADOR 1')
            continue

        elif compraCartaJogador2 == 0:
            if len(cartasDescartadasJogador1) < 1:
                print('*'*90)
                print('O outro jogador ainda não descartou uma carta')
                print('*' * 90)
                continue
            elif len(cartasDescartadasJogador1) >= 1:
                cartasDescartadasExtenso2 = int(input(
                    f'Digite 0 - para descartar a carta {jogador_2[0]}\nDigite 1 - para descartar a carta {jogador_2[1]}\nDigite 2 - para descartar a carta {jogador_2[2]} \n:'))

                if cartasDescartadasExtenso2 == 0:
                    deleta(jogador_2)
                    pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 0, -1)
                    mostraCartas(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria()
                    if true != 1:
                        continue

                elif cartasDescartadasExtenso2 == 1:
                    deleta(jogador_2)
                    pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 1, -1)
                    mostraCartas(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria()
                    if true != 1:
                        continue

                elif cartasDescartadasExtenso2 == 2:
                    deleta(jogador_2)
                    pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 2, -1)
                    mostraCartas(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria()
                    if true != 1:
                        continue
    true1 = 1

    #VEZ JOGADOR 2 NÃO CONDICIONAL
    while true1 == 1:
            print('         OK VEZ DO JOGADOR 2')
            print(
                'Voce pode descartar uma carta e comprar uma, não fazer nada ou descartar uma carta epegar a ultima carta descartada do outro jogador. DIGITE APENA OS NUMEROS! \n')
            mostraCartas(jogador_2)
            compraCartaJogador2 = int(input(
                'Digite 2 - para descartar uma carta e comprar outra do baralho\nDigite 1 - para não fazer nada\nDigite 0 - Para descartar uma carta e pegar outra carta descartada do jogador 1\n: '))
            if compraCartaJogador2 == 2:
                print('*' * 90)
                mostraCartas(jogador_2)
                cartasDescartadasExtenso2 = int(input(
                    f'Digite 0 - para descartar a carta {jogador_2[0]}\nDigite 1 - para descartar a carta {jogador_2[1]}\nDigite 2 - para descartar a carta {jogador_2[2]} \n:'))
                if cartasDescartadasExtenso2 == 0:
                    compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 0)
                    mostraCartas(jogador_2)
                    deleta(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria2()
                    if true1 == 1:
                        true1 = 0
                        continue
                    else:
                        true = 0
                        true1 = 0
                        break
                elif cartasDescartadasExtenso2 == 1:
                    compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 1)
                    deleta(jogador_2)
                    mostraCartas(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria2()
                    if true1 == 1:
                        true1 = 0
                        continue
                    else:
                        true = 0
                        true1 = 0
                        break
                elif cartasDescartadasExtenso2 == 2:
                    compraDescartaJogador(jogador_2, cartasDescartadasJogador2, 2)
                    deleta(jogador_2)
                    mostraCartas(jogador_2)
                    somadorDePontosJogador2()
                    CondicoesDeVitoria2()
                    if true1 == 1:
                        true1 = 0
                        continue
                    else:
                        true = 0
                        true1 = 0
                        break
            elif compraCartaJogador2 == 1:
                print('     OK VEZ DO JOGADOR 1')
                true1 = 0
                continue
            elif compraCartaJogador2 == 0:
                if len(cartasDescartadasJogador1) < 1:
                    print('*' * 90)
                    print('O outro jogador ainda não descartou uma carta')
                    print('*' * 90)
                    continue
                elif len(cartasDescartadasJogador1) >= 1:
                    cartasDescartadasExtenso2 = int(input(
                        f'Digite 0 - para descartar a carta {jogador_2[0]}\nDigite 1 - para descartar a carta {jogador_2[1]}\nDigite 2 - para descartar a carta {jogador_2[2]} \n:'))
                    if cartasDescartadasExtenso2 == 0:
                        deleta(jogador_2)
                        pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 0, -1)
                        mostraCartas(jogador_2)
                        somadorDePontosJogador2()
                        CondicoesDeVitoria2()
                        if true1 == 1:
                            true1 = 0
                            continue
                        else:
                            true = 0
                            true1 = 0
                            break
                    elif cartasDescartadasExtenso2 == 1:
                        deleta(jogador_2)
                        pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 1, -1)
                        mostraCartas(jogador_2)
                        somadorDePontosJogador2()
                        CondicoesDeVitoria2()
                        if true1 == 1:
                            true1 = 0
                            continue
                        else:
                            true = 0
                            true1 = 0
                            break
                    elif cartasDescartadasExtenso2 == 2:
                        deleta(jogador_2)
                        pegarUltimaCartaDescartada(jogador_2, cartasDescartadasJogador1, 2, -1)
                        mostraCartas(jogador_2)
                        somadorDePontosJogador2()
                        CondicoesDeVitoria2()
                        if true1 == 1:
                            true1 = 0
                            continue
                        else:
                            true = 0
                            true1 = 0
                            break