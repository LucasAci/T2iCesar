# Uma loja tem 150 clientes e deseja enviar uma mensagem oferecendo
# um bônus de natal para cada um deles;
# O algoritmo deverá ler o nome do cliente e o
# valor total de suas compras no ano;
# Se o valor das compras for menor que R$5.000,00,
# calcular um bônus de 10% sobre o valor das compras;
# Se o valor for igual ou maior que R$5.000,00,
# calcular um bônus de 15%;
#  Imprimir para cada cliente:
#  “PREZADO <NOME>, VOCÊ POSSUI R$<VALOR DO BONUS> EM NOSSA LOJA”.

CLIENTES = 150 # para teste, utilize 3.

for cliente in range (CLIENTES):
    nome = (input("Digite o nome: "))
    valorCompras = float(input("Digite o valor total das compras: "))
    if valorCompras < 5000:
        bonus = valorCompras * 0.1
    else:
        bonus = valorCompras * 0.15
    print(f"Prezado {nome}, você possui R${bonus} em nossa loja.")






