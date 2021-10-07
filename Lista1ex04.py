# Faça um programa que imprima na tela apenas os números ímpares entre 0 e 50.

num = 0

while num < 50:
    num = num + 1
    if num % 2 == 1:
        print(f"{num}")