# Faça um programa que:
# Leia a idade de 4 pessoas.
# Após esta entrada de dados, exiba:
# i) As idades armazenadas;
# ii) Média das idades;
# iii) Maior e menor idade (pode usar max e min);

idades = []
media = 0

for i in range(4):
    idades.append(int(input(f" idade da {i+1} pessoa: ")))

    media = sum(idades) / len(idades)
maxino = max(idades)
minimo = min(idades)

print(f"idades Armazenadas: {idades}")
print(f"Média das idades: {media}")
print(f"Maior idade: {maxino}")
print(f"Menor idade: {minimo}")


