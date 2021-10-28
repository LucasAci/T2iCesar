# Faça um programa que solicite a idade de 5 pessoas
# e calcule a média.

soma = 0
QUANTIDADE = 5
for i in range (QUANTIDADE):   # O i está servindo para contar
    idade = int(input("Digite a idade: "))
    soma = soma + idade

media = soma / QUANTIDADE

print(f"A média das idades é: {media}")

