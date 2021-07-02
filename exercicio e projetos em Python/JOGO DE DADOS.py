'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios;
Guarde esses resultados em um dicionário;
Coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}

ranking = list()                        # organizar para mostrar em ordem quem ganhou

print('valores sorteados')

for k,v in jogo.items():                # Mostrar o que cada um tirou nos dados
    print(f'o {k} tirou {v} no dado')
    sleep(0.5)

#  PRIMEIRO EU ORGANIZO (); MAS PARA ISSO EU PRECISO SEPARAR CHAVES DE VALORES( JOGO.ITEMS())
#  APÓS ISSO, EU PRECISO SOMENTE DA KEY = A FUNÇÃO ITEMGATTER NO ELEMENTO 1( 0= CHAVES, 1 = VALORES)
#  DEPOIS, SÓ REVERTER OS VALORES

ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('=-'*50)
print(f'    RANK DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} tirou {v[1]}')
    sleep(0.5)

