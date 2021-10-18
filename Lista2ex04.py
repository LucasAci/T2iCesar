# Faça um programa que leia o nome, idade e altura de 5 pessoas. O sistema
# deverá apresentar o nome, idade e altura da pessoa mais alta.

idadeMaisAlto = 0
maiorAltura = 0
nomeMaisAlto = ""

for pessoa in range(5):
    nome = (input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    if altura > maiorAltura:
        maiorAltura = altura
        nomeMaisAlto = nome
        idadeMaisAlto = idade

print(f"{nomeMaisAlto}, com {idadeMaisAlto} anos e {maiorAltura}m, é a pessoa mais alta do grupo.")
