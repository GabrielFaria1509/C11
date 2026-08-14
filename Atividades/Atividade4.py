#Atividade 4 (Cap 4 exercícios partes 1 e 2)

import numpy as np

arr1 = np.ones(8)
arr2 = np.random.randint(0,10,8)
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")

arr3 = arr1 + arr2
print(f"Array 3 (soma): {arr3}")
 ##Vericiando se a soma dos elementos é maior ou igual à 40
if np.sum(arr3) >= 40:
    print("A soma dos elementos do array 3 eh maior ou igual a 40")
    mtz = arr3.reshape(4,2)
    print(f"Matriz 4x2(mais linhas, menos colunas): \n{mtz}")
else:
    print("A soma dos elementos do array 3 eh menor que 40")
    mtz = arr3.reshape(2,4)

#Exercício 2

#imprimo pares de 0 a 50
arr_par = np.arange(0,52,2)
print(f"Array de pares de 0 a 50: {arr_par}")

#Uso 48 pois é exclusivo, então o último número par que quero é 50
arr_par2 = np.arange(100,48,-2)
print(f"Array de pares de 100 a 50: {arr_par2}")

arr_concat = np.concatenate((arr_par, arr_par2))
print(f"Array concatenado: {arr_concat}")
print(f"Array concatenado em ordem crescente: {np.sort(arr_concat)}")


#Exercício 3

mtz = np.zeros((2,2))
print(f"Matriz base: \n{mtz}")

#Adicionando 1 em uma posição aleatória da matriz
i = np.random.randint(0,2)
j = np.random.randint(0,2)

k = np.random.randint(0,2)
l = np.random.randint(0,2)

mtz[i][j] = 1
mtz[k][l] = 1
vidas = 3
um_encontrados = 0

bomba1_achada = False
bomba2_achada = False

linha_selecionada = int(input("Digite a linha que deseja selecionar (0 ou 1): "))
coluna_selecionada = int(input("Digite a coluna que deseja selecionar (0 ou 1): "))

while vidas > 0:
    if linha_selecionada == i and coluna_selecionada == j and not bomba1_achada:
        print("Você acertou!")
        bomba1_achada = True
        um_encontrados += 1
    elif linha_selecionada == k and coluna_selecionada == l and not bomba2_achada:
        print("Você acertou!")
        bomba2_achada = True
        um_encontrados += 1
    else:
        vidas -= 1
        print(f"Você errou! Vidas restantes: {vidas}")

    if um_encontrados == 2:
        print("Parabéns! Você encontrou todas as bombas!")
        break

    if vidas > 0:
        linha_selecionada = int(input("Digite a linha que deseja selecionar (0 ou 1): "))
        coluna_selecionada = int(input("Digite a coluna que deseja selecionar (0 ou 1): "))
    else:
        print("Suas vidas acabaram! Você perdeu.")

#Exercício 4
linha_number = np.random.randint(0,11)
coluna_number = np.random.randint(0,11)

mtz_result = np.random.randint(0,10,(linha_number,coluna_number))

print(f"Matriz criada : \n{mtz_result}")

produto = linha_number*coluna_number

#Verifico se consigo transformar em um vetor unidimensiol com um número par de elementos

resto = produto%2

if resto == 0 : 
    print("Matriz pode ser transformada em um vetor de número par de elementos")
else:
    print("Matriz não pode ser transformada em um vetor de número par de elementos, somente ímpar")

#Exercício 5

np.random.seed(10)
mtz_aleat = np.random.randint(1,51,(4,4))
print(f"Matriz gerada : \n{mtz_aleat}")

for i in range(0,4):
    print(f"Média da coluna {i+1} : {mtz_aleat.mean(axis=0)[i]}")
    print(f"Média da linha {i+1} : {mtz_aleat.mean(axis=1)[i]}")

medias_colunas = mtz_aleat.mean(axis=0)  
medias_linhas = mtz_aleat.mean(axis=1)   

media_max_coluna = medias_colunas.max()
media_max_linha = medias_linhas.max()

#Contagem elementos da matriz
elemento,contagem = np.unique(mtz_aleat,return_counts=True)
#elemento2vezes = elemento[contagem==2]
for e,c in zip(elemento,contagem):   #Zip junta dois arrays/listas elemento por elemento
    if c == 2:
        print(f"Elemento ({e}) encontrado 2 vezes")
















