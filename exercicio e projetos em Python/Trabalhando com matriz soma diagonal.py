'''
2.7 – Crie um programa que calcule a soma dos elementos da diagonal principal.
'''

a = [[1,7,8,10],
     [3,6,9,11],
     [5,4,2,0],
     [12,3,8,9]]

soma = 0
for l in range(0, len(a)):
    for c in range(0, len(a[l])):
        if l == c:
            soma += a[l][c]
print(f' A soma dos elementos da diagonal principal é {soma}')

