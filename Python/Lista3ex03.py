# Faça um programa em duas partes:
# Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
# Parte 02: Em uma nova estrutura de repetição, armazene os números pares na
# lista PARES e os números ímpares na lista ÍMPARES.
# Imprima as três listas.

numeros = []
numerosPares = []
numerosImpares = []

for i in range(10):
    numeros.append(int(input("Digite o número: ")))

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numerosPares.append(numeros[i])
    else:
        numerosImpares.append(numeros[i])

print(f"Numeros: {numeros}")
print(f"Pares: {numerosPares}")
print(f"Ímoares: {numerosImpares}")




