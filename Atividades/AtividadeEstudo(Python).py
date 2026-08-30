import math as mt
nome = str(input("Digite seu nome :  "))
idade = int(input("Digite sua idade :  "))
cidade = str(input("Digite cidade que mora :  "))

print(f"Meu nome é {nome}, moro em {cidade}, e tenho {idade} anos")

celsius = int(input("Digite temperatura em celsius :  "))
fahren = (celsius*(9/5)) + 32
print(f"Temperatura em F : {fahren:.2f}")

a = 15
b = 7.5
c = True
d = "Python"
print(f"Tipos das variáveis a,b,c,d : {type(a),type(b),type(c),type(d)}")

num= int(input("Digite um número : "))
num2 = int(input("Digite um número : "))

print(f"Divisão : {num/num2}")
print(f"Divisão inteira : {mt.trunc(num/num2)}")
print(f"Resto da divisão : {num%num2}")
print(f"Potência : {num**num2}")

print(f"Antecessor de num : {num-1}")
print(f"Sucessor de num : {num+1}")
print(f"Dobro de num : {num*2}")
print(f"Triplo de num : {num*3}")

num,num2 = num2,num
print(f"Valores após troca -> num : {num} num2 : {num2}")

lado = int(input("Digite o valor do lado : "))
area = lado*lado
print(f"Aréa : {area}")
print(f"Aréa : {mt.sqrt(area)}")
print(f"Aréa : {mt.ceil(area)}")
print(f"Aréa : {mt.floor(area)}")

print(f"Fatorial do valor de lado : {mt.factorial(lado)}")

palavra = str(input("Digite uma palavra : "))
print(f"Primeiro caractere : {palavra[0]}")
print(F"Último caractere : {palavra[-1]}")
print(f"1 a 3 caracteres : {palavra[0:3]}")
print(f"3 últimos caracteres : {palavra[-1:-4]}")
print(f"Palavra invertida : {palavra[::-1]}")


frase = str(input("Digite uma frase : "))
print(f"Quantidade de caracteres : {len(frase)}")
print(f"Quantidade de espaços : {frase.count(" ")}")
print(f"Primeira ocorrência letra a : {frase.find("a")}")
print(f"Frase em maiúscula : {frase.upper()}")
print(f"Frase em minúsculo : {frase.lower()}")








