# Faça um programa que receba notas de alunos, até -1 ser informado.
# Ao final da execução, o programa deve exibir quantas notas foram informadas e a média entre elas.

nota = 0.0
totalNotas= 0
i = 0
media = 0.00
while nota != -1:
    nota = float(input("Digite uma nota ou -1 para finalizar: "))
    if nota != -1:
        i = i + 1
        totalNotas = totalNotas + nota

media = totalNotas / i
print(f"Foram informadas {i} notas e a média é {media}")

