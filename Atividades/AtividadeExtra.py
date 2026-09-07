import math as mt
import numpy as np

#Questão 1

lista_dicionario = []

mais_antiga = 99999
nome_mais_antiga = None

while True:
    nome_musica = input("Digite o nome da música (ou 'sair' para encerrar): ")
    if nome_musica.lower() == 'sair':
        break
    else:
        ano_lancamento = int(input("Digite o ano de lançamento da música: "))
        dicionario_musica = {
            'nome': nome_musica,
            'ano': ano_lancamento
        }
        if ano_lancamento < 0:
            print("Ano de lançamento inválido. Por favor, insira um ano válido.")
            ano_lancamento = int(input("Digite o ano de lançamento da música: "))
            continue
        lista_dicionario.append(dicionario_musica)

print("\nLista de músicas cadastradas:")
for musica in lista_dicionario:
    print(f"Nome: {musica['nome']}, Ano de Lançamento: {musica['ano']}")
    if musica['ano'] < mais_antiga:
        mais_antiga = musica['ano']
        nome_mais_antiga = musica['nome']

print(f"\nMúsica mais antiga: {nome_mais_antiga}, Ano: {mais_antiga}")

#Questão 2

nomes_1 = np.array(['Dante', 'Vergil', 'Nero', 'Sparda'])
nomes_2 = np.array(['Maya', 'Fl4K', 'Lillith', 'Jack'])

nomes_geral = np.concatenate((nomes_1, nomes_2))
print(f"Array concatenado: \n{nomes_geral}")

nomes_geral_ordenados_decreescentes = np.sort(nomes_geral)[::-1]
print(f"Array ordenado em ordem decrescente: \n{nomes_geral_ordenados_decreescentes}")

matriz_nomes = nomes_geral.reshape(4, 2)
print(f"Matriz 4x2: \n{matriz_nomes}")

#Questão 3

colors = [
  { "color": "black", "type": "primary", "code": { "rgba": [255, 255, 255, 1], "hex": "#000" } },
  { "color": "green", "type": "secondary", "code": { "rgba": [0, 255, 0, 1], "hex": "#0F0" } },
  { "color": "yellow", "type": "primary", "code": { "rgba": [255, 255, 0, 0.7], "hex": "#FF0" } },
  { "color": "blue", "type": "primary", "code": { "rgba": [0, 0, 255, 1], "hex": "#00F" } }
]

for color in colors:
    if color["type"] == "primary":
        print(f"Cor: {color['color']}, Tipo: {color['type']}, Código RGBA: {color['code']['rgba']}, Código HEX: {color['code']['hex']}")

for color in colors : 
    if color["code"]["rgba"][2] == 255:
        print(f"Cor: {color['color']}, Tipo: {color['type']}, Código RGBA: {color['code']['rgba']}, Código HEX: {color['code']['hex']}")

lista_nome_hex = []
for color in colors : 
    lista_nome_hex.append(color["color"])
    lista_nome_hex.append(color["code"]["hex"])

np_array_nome_CodigoHexadecimal = np.array(lista_nome_hex)

print(f"Array NumPy com os códigos hexadecimais e nome: \n{np_array_nome_CodigoHexadecimal}")

print(f"tamanho do array NumPy : {len(np_array_nome_CodigoHexadecimal)}")
matriz_4x2 = np_array_nome_CodigoHexadecimal.reshape(4, 2)
print(f"Matriz 4x2: \n{matriz_4x2}")

matriz_4x2 = matriz_4x2.astype("<U10")

traducao_cores = {
    "black": "preto",
    "green": "verde",
    "yellow": "amarelo",
    "blue": "azul"
}

for linha in matriz_4x2:
    linha[0] = traducao_cores[linha[0]]

print(f"Matriz 4x2 com cores traduzidas: \n{matriz_4x2}")



