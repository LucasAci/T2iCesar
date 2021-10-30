# Faça um programa que:
# Receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Calcule a média anual de temperaturas
# Exiba todos os meses que têm as temperaturas acima da média anual (mostrar o
# mês por extenso: Janeiro, Fevereiro, . . . ). Dica: Crie uma lista de strings com
# todos os nomes dos meses.

temperatura = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]
media = 0
soma = 0
acimaMedia = {}

for i in range(len(meses)):
    temperatura.append(float(input(f" Informe a temperatura média do mês de {meses[i]} :\n ")))
    soma = soma + temperatura[i]
    media = soma / len(meses)

for i in range(len(meses)):
    if temperatura[i] > media:
        acimaMedia.update({meses[i]: temperatura[i]})


print(f"Média anual de temperatura: {media}")
print(f"meses com temperaturas acima da média: {acimaMedia}")
