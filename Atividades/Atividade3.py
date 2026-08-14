
print("A acentuação sairá normalmente se usar um terminal que suporte UTF-8 ou um terminal dedicado a Python")

#Exercício 1
times = ["Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern de Munique"]
print("Primeiro colocado :  {} , segundo colocado : {} , terceiro colocado : {}".format(times[0], times[1], times[2]))
print("Últimos colocados : {}, {}".format(times[3], times[4]))

# deixando em ordem alfabética
times_alf = tuple(sorted(times))
print(times_alf)

position_barcelona = times.index("Barcelona")
print("Posição de Barcelona na tupla : {}".format(position_barcelona))

#Exercíco 2

loja1 = {"Samsung A55","Samsung M55","Samsung S25"}
loja2 = {"Iphone 14","Iphone 15","Iphone 16","Samsung S25"}

print("Produtos disponíveis na loja 1 : {}".format(loja1))
print("Produtos disponíveis na loja 2 : {}".format(loja2))

print("Produtos disponíveis no total ao visistar ambas as lojas : {}".format(loja1.union(loja2)))
print("Produtos disponíveis em ambas as lojas : {}".format(loja1.intersection(loja2)))

#Exercício 3

nome = str(input("Digite seu nome: "))
media = int(input("Digite sua média: "))

aluno = {
    "nome": nome,
    "media": media
}

if aluno["media"] >= 50 :
    print("Aluno aprovado com média : {}".format(aluno["media"]))
    aluno["Status"] = "Aprovado"
else:
    print("Aluno reprovado com média : {}".format(aluno["media"]))
    aluno["Status"] = "Reprovado"

print(f"Fichário do aluno : {aluno}")#Alternativa ao print("Fichário do aluno : {}".format(aluno))

#Exercício 4

nome_pessoa1 = str(input("Digite o nome da primeira pessoa: "))
peso_pessoa1 = float(input("Digite o peso da primeira pessoa: "))

nome_pessoa2 = str(input("Digite o nome da segunda pessoa: "))
peso_pessoa2 = float(input("Digite o peso da segunda pessoa: "))

nome_pessoa3 = str(input("Digite o nome da terceira pessoa: "))
peso_pessoa3 = float(input("Digite o peso da terceira pessoa: "))




#Uso de uma lista de deicionários para armazenar os dados das pessoas, peso pode mudar etc
#Crio dicionário das pessoas
pessoa1 = {
    "nome": nome_pessoa1,
    "peso": peso_pessoa1
}
pessoa2 = {
    "nome": nome_pessoa2,
    "peso": peso_pessoa2
}
pessoa3 = {
    "nome": nome_pessoa3,
    "peso": peso_pessoa3
}

pessoas = [pessoa1, pessoa2, pessoa3]



maior_peso = max(pessoas, key = lambda p: p["peso"])
menor_peso = min(pessoas, key = lambda p: p["peso"])

#Jeito alternativo
#cont = 0
#dados = {}

#While(cont<3)
#nome = input("Nome : ")
#peso = input(int("Peso : "))
#dados[nome] = peso
#cont+=1
#mais_pesado = max(dados, key = dados.get)
#mais_leve = min(dados, key = dados.get)

# key=lambda diz ao max() e min() para comparar os dicionários
# pelo valor de "peso" de cada um, e não pelo dicionário inteiro

# lambda é uma forma de criar uma função rápida, sem usar def

# p é o parâmetro da função lambda, representa cada pessoa da lista
# p["peso"] é o valor que a função retorna (o peso daquela pessoa)

print(f"A pessoa com maior peso é {maior_peso['nome']} com {maior_peso['peso']} kg")
print(f"A pessoa com menor peso é {menor_peso['nome']} com {menor_peso['peso']} kg")

#Exercício 5

quantidade = int(input("Digite a quantidade de pessoas: "))

contador_mulheres_menores_20 = 0
soma_idades = 0
for i in range(0,quantidade):
    nome = str(input("Digite o nome da pessoa {}: ".format(i+1))) #Adiciono o i+1 para que a contagem comece em 1 e não em 0
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    sexo = str(input("Digite o sexo da pessoa {} (M/F): ".format(i+1)))
    pessoa = { #Cada input vai atualizando o dicionário pessoa, que é adicionado à lista pessoas
        "nome": nome,
        "idade": idade,
        "sexo": sexo
    }
    pessoas.append(pessoa) #Adiciono no final da lista pessoas o dicionário pessoa, que contém os dados da pessoa atual
    soma_idades += idade #Soma as idades para calcular a média depois

    #Seleciono somente as mulhere com menos de 20 anos, e adiciono em uma lista separada
    if sexo == "F" and idade < 20:
        contador_mulheres_menores_20 += 1

print(f"Quantidade de mulheres com menos de 20 anos: {contador_mulheres_menores_20}")
print(f"Média das idades: {soma_idades/quantidade:.2f}") #:.2f formata o número para 2 casas decimais

#Exercício 6
ingredientes_receita_bolo = ["Farinha de trigo", "Açúcar", "Ovos", "Leite", "Fermento em pó"]
ingredientes_receita_bolo.append("Manteiga") #Adiciona manteiga no final da lista
ingredientes_receita_bolo[3] = "Leite integral" #Substitui leite por leite integral
#Removendo pelo index
del ingredientes_receita_bolo[2] #Remove ovos da lista

itens_pessoa1 = {"Farinha de trigo", "Açúcar", "Ovos"}
itens_pessoa2 = {"Leite", "Fermento em pó", "Manteiga"}

#junto os itens das duas pessoas e verifico se a receita está completa
ingredientes_completos = itens_pessoa1.union(itens_pessoa2)

#set transforma a lista em um conjunto, que não permite elementos duplicados
ingredientes_faltando = set(ingredientes_receita_bolo) - ingredientes_completos
print(f"Ingredientes faltando para a receita: {ingredientes_faltando}")

nome_produto1 = str(input("Digite o nome do produto 1: "))
preco_produto1 = float(input("Digite o preço do produto 1: "))
quantidade_produto1 = int(input("Digite a quantidade do produto 1: "))

nome_produto2 = str(input("Digite o nome do produto 2: "))
preco_produto2 = float(input("Digite o preço do produto 2: "))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = str(input("Digite o nome do produto 3: "))
preco_produto3 = float(input("Digite o preço do produto 3: "))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: "))

produto1 = {
    "nome": nome_produto1,
    "preco": preco_produto1,
    "quantidade": quantidade_produto1
}
produto2 = {
    "nome": nome_produto2,
    "preco": preco_produto2,
    "quantidade": quantidade_produto2
}
produto3 = {
    "nome": nome_produto3,
    "preco": preco_produto3,
    "quantidade": quantidade_produto3
}

dados_produtos = [produto1, produto2, produto3]

print("Dados dos produtos:")
for produto in dados_produtos: #uso de for it
    print(f"Produto: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

print("Valor em estoque de cada produto:")
for produto in dados_produtos:
    valor_estoque = produto['preco'] * produto['quantidade']
    print(f"Produto: {produto['nome']}, Valor em estoque: {valor_estoque:.2f}")

