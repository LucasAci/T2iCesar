# faça um algoritmo que receba vários números positivos até o
# usuário digitar -1 e finalizar. Por fim exiba a quantidade de
# números válidos digitados.

num = 0
i = 0
while num != -1:
    num = int(input("Digite um número positivo ou -1 para finalizar: "))
    if num != -1:
        i = i + 1
    print(f"Você digitou {i} numeros.")
