# Faça um programa que leia 10 números inteiros e exiba-os em ordem crescente.

numeros = []
QUANTIDADE = 10

for i in range(QUANTIDADE):
    numeros.append(int(input("Digite o número: ")))

numeros.sort()
print(f"Números em ordem crescente: {numeros}")

