# Ler as notas de 5 alunos, calcular e informar a média da turma.

ALUNOS = 5
soma_nota = 0
for i in range(ALUNOS):
    nota = float(input('Digite a nota: '))
    soma_nota = soma_nota + nota

media = soma_nota / ALUNOS
print(f'A média da turma é {media}')
