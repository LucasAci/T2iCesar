# Faça um programa que:
# a) Leia 5 idades e armazene-as em uma lista.
# b) Em uma nova estrutura de repetição, armazene as idades >= 18 na lista MAIORES
# e as idades < 18 na lista MENORES
# c) Imprima as três listas.

idades = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    idades.append(int(input("Digite a idade: ")))

maiores = []
menores = []
for i in range(len(idades)):
    if idades[i] >= 18:
        maiores.append(idades[i])
    else:
        menores.append(idades[i])
print(f"Idades: {idades}")
print(f"Idades >= 18: {maiores}")
print(f"Idades < 18: {menores}")