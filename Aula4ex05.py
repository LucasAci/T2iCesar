# Faça um programa que receba a idade de 5 pessoas e
# ao final da execução apresente a menor e a maior idade informada.

menorIdade = 0
maiorIdade = 0

for pessoa in range(5):
    idadeAtual = int(input("Digite a idade: "))

    if pessoa == 0:
        menorIdade = idadeAtual
    elif idadeAtual < menorIdade:
        menorIdade = idadeAtual
    elif idadeAtual > maiorIdade:
        maiorIdade = idadeAtual


print(f"A menor idade informada é: {menorIdade} e a maior idade é: {maiorIdade}")
