# Faça um programa que imprima a soma de todos os números pares
# entre dois números informados pelo usuário.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número (deve ser maior que o primeiro: "))

somaPares = 0
for num in range(num1, num2):
    if num % 2 == 0:
        somaPares = somaPares + num

print(f"A soma dos números é: {somaPares}")
