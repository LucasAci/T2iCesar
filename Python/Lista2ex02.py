# 2 -Um petshop atende 10 cachorros por tarde. Faça um programa que solicite ao
# usuário o nome do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa; 4-
# outros). Por fim, exiba a quantidade de solicitações para cada um deles.


contadorBanho = 0
contadorTosa = 0
contadorBanhoTosa = 0
contadorOutros = 0
for i in range (10):

    servico = int(input("Solicite um serviço: 1-Banho, 2-Tosa, 3-Banho e tosa, 4-Outros: "))
    if servico == 1:
        contadorBanho = contadorBanho + 1

    elif servico == 2:
        contadorTosa = contadorTosa + 1

    elif servico == 3:
        contadorBanhoTosa = contadorBanhoTosa + 1

    elif servico == 4:
        contadorOutros = contadorOutros + 1

print(f"Banho: {contadorBanho}\nTosa: {contadorTosa}\nBanho e tosa: {contadorBanhoTosa}\nOutros: {contadorOutros}")