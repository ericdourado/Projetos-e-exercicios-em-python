'''
3.2 - Faça um programa que imprima os índices do dicionários em que os valores são negativos.

'''

dicionario = {'a':1, 'b':2, 'c':3, 'd':-1, 'e':-3, 'f':6, 'g':4}

for chave in dicionario:
    if dicionario[chave] < 0:
        print(f'a chave "{chave}" possui valor negativo')