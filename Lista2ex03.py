# Faça um algoritmo que solicite um valor inicial, um valor final e exiba todos os
# números pares entre os dois (incluindo-os).

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número, que seja maior que o anterior: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)