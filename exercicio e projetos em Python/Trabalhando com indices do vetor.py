'''

Crie um programa que some os índices pares com os indices ímpares do do vetor

'''

vetor = [1, -5, 0, 3, 9, -1, 7]
somaPar = 0
somaImpar = 0
for x in range(0,len(vetor)):
    if x % 2 == 0:
        somaPar+= vetor[x]
    else:
        somaImpar+= vetor[x]

print(f'Soma dos numeros pares: {somaPar}')
print(f'Soma dos numeros impares: {somaImpar}')