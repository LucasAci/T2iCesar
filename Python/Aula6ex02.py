# Faça um programa que armazene 5 idades em uma lista e, por fim, as exiba,
# uma abaixo da outra.

idades = []
for i in range(5):
    idades.append(int(input('Digite a idade: ')))

for i in range(5):
    print(f'A idade no index {i} é {idades[i]}')
