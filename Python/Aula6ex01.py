# Informe o nome e idade de 3 pessoas. Após inserir as informações,
# busque pelo nome de uma pessoa.
# Se ela existir no sistema:
# pergunte se o usuário deseja removê-la.
#  - Caso positivo, ocorrerá a remoção
#  - Caso negativo, a pessoa não será removida do programa.
# Se a pessoa não existir no programa, exiba:
# "Usuário não encontrado!".
# Por fim, todas as informações das pessoas cadastradas devem ser exibidas.

nomes = []
idades = []

for i in range(3):
    nomes.append(input("Digite o nome: "))
    idades.append(int(input("Digite a idade: ")))

pessoa = input("Digite o nome da pessoa que você deseja Remover: ")

if pessoa in nomes:
    pergunta = input(f"Você deseja excluir {pessoa}: ?\nS - Sim ou N - Não")
    if pergunta == "S":
        posicao = nomes.index(pessoa)# procura a posição da pessoa
        nomes.pop(posicao) # deletei a pessoa na posição
        idades.pop(posicao)# deletei a idade na posição
        print("Usuário removido com sucesso!!")

else:
    print("Usuário não encontrado!")

print(f"Nomes cadastrados: {nomes} \nIdades cadastradas: {idades}")

