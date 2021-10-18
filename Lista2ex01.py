# 1- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
# de números pares e a quantidade de números ímpares.

contadorPar = 0
contadorImpar = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        contadorPar = contadorPar + 1
    elif num % 2 == 1:
        contadorImpar = contadorImpar + 1

print(f"Pares: {contadorPar}")
print(f"Ímpares: {contadorImpar}")


