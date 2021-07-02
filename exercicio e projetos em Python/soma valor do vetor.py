'''
Considere o vetor V = [1, -5, 0, 3, 9, -1, 7]:
2.3 – Crie um algortimo que some todos os valores de V e imprima o valor da soma.
'''

vetor = [1, -5, 0, 3, 9, -1, 7]
somaVetor = 0

for x in range(0, len(vetor)):
    somaVetor += vetor[x]
print(f'A soma de todos os valores do vetor é: {somaVetor}')