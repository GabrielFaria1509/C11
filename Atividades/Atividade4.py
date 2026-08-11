#Atividade 4 (Cap 4 exercícios partes 1 e 2)

import numpy as np

#Exercício 1
arr1 = np.ones(8)
arr2 = np.random.randint(0,10,8)
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")

arr3 = arr1 + arr2
print(f"Array 3 (soma): {arr3}")
 ##Vericiando se a soma dos elementos é maior ou igual à 40
if np.sum(arr3) >= 40:
    print("A soma dos elementos do array 3 eh maior ou igual a 40")
    mtz = np.reshape(arr3,(4,2))
    print(f"Matriz 4x2(mais linhas, menos colunas): \n{mtz}")
else:
    print("A soma dos elementos do array 3 eh menor que 40")
    mtz = np.reshape(arr3,(2,4))
    print(f"Matriz 2x4(menos linhas, mais colunas): \n{mtz}")