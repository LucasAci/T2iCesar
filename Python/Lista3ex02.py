# Faça um programa que:
# Peça duas notas de 5 estudantes.
# Calcule e armazene numa lista a média de cada estudante.
# Imprima a lista de médias e o número de estudantes com média >= 7.0.

media = []
contador = 0
for i in range(5):
    nota1 = float(input(f"Estudante {i+1}, digite a primeira nota: "))
    nota2 = float(input(f"Estudante {i+1}, digite a segunda nota: "))
    mediaAlunos = float((nota1 + nota2) / 2)
    media.append(mediaAlunos)

print(f' Média: {media}')

for i in range(len(media)):
    if media[i] >= 7:
        contador = contador + 1
print(f"Números de estudantes com média >= 7: {contador}")












