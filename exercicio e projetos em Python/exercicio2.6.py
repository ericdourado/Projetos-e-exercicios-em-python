'''
2.6 – Crie um programa que calcule a soma dos elementos da primeira coluna da matriz
'''
a = [[1,7,8,10],
     [3,6,9,11],
     [5,4,2,0],
     [12,3,8,9]]

soma = 0

for l in range(0, len(a)):
     soma += a[l][0]
print(f'A soma dos elementos da primeira coluna da matriz é {soma}')