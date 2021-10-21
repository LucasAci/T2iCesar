# Faça duas listas para armazenar as idades e alturas de 5 alunos
# O programa deverá determinar quantos alunos com mais de 13 anos
# possuem altura inferior à média das alturas dos alunos.

idades = []
alturas = []
contador = 0

for i in range(5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))

mediaAltura = sum(alturas) / len(alturas)

for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < mediaAltura:
        contador += 1
print(f"A média das alturas é: {mediaAltura}")
print(f"A quantidade de pessoas maiores de 13 anos com altura inferior a média é: {contador}")

