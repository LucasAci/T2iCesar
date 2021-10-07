#Faça um algoritmo que leia duas notas e informe se o estudante está:
#- aprovado, caso a média seja maior ou igual a 7
#- final, caso a média seja maior ou igual a 4 e menor que 7
#- reprovado, caso a média seja menor que 4


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if media >= 7:
    print(f"APROVADO!")
elif media >= 4 and media<7:
    print(f"FINAL!")
else:
    print(f"REPROVADO")