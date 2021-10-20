# Ler as notas de 5 alunos, calcular e informar a média;
# Imprimir as notas que são superiores a média da turma.

notas = []
for i in range(5):
    notas.append(float(input('Digite a nota: ')))

media = sum(notas) / len(notas)
print(f'A média da turma é {media}')

for i in range(5):
    if notas[i] >= media:
        print(notas[i])



