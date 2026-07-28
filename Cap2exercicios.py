import math

#Exercício 1
#Use Gabriel faria Monteiro
nome = input("Digite seu nome: ");
print(nome.upper()); #Maiusculo
print(nome.lower()); #Minísculo
print(len(nome)); #Quantidade de caracteres
print(nome.replace("Monteiro","do Inatel")); #Substituição de palavras


#Exercçio 2
num = int(input("Digite um número: ")); #número base
begin = int(input("Digite o início do intervalo: ")); #intervalo
end = int(input("Digite o fim do intervalo: "));
print("Tabauda do {} no intervalo de {} a {}:".format(num,begin,end));
if begin > end:
    begin,end = end,begin
for c in range(begin,end+1): #adiciona mais um por ser exclusivo o final do range(subtrtai 1 do final do intervalo)
    print("{} x {} = {}".format(num,c,num*c));

#Exercício 3
sexo = ""
while sexo!="M" and sexo!="F":
    sexo = input("Digite seu sexo (M/F): ").upper();
    if sexo!="M" and sexo!="F":
        print("Sexo inválido. Digite novamente.");

#Exercício 4
dist = float(input("Digite a distância em Km da viagem : "));
if dist <= 200:
    custo = dist * 0.50;
    print("O preço da viagem é R$ : {}".format(custo));
else:
    custo = dist * 0.45;
    print("O preço da viagem é R$ : {}".format(custo));

#Exercício 5
number = int(input("Digite um número: "));
if number < 10:
    print("Número da unidade : {}".format(number % 10));
    print("Não há dezena, centena e milhar");
if number >= 10 and number < 100:
    print("Número da unidade : {}".format(number % 10));
    print("Número da dezena : {}".format((number // 10) % 10));
    print("Não há centena e milhar");
if number >= 100 and number < 1000:
    print("Número da unidade : {}".format(number % 10));
    print("Número da dezena : {}".format((number // 10) % 10));
    print("Número da centena : {}".format((number // 100) % 10));
    print("Não há milhar");
if number >= 1000:
    print("Número da unidade : {}".format(number % 10));
    print("Número da dezena : {}".format((number // 10) % 10));
    print("Número da centena : {}".format((number // 100) % 10));
    print("Número do milhar : {}".format((number // 1000) % 10));

#Exercício 6
num = float(input("Digite um número: "));
print("Raiz quadrada : {}".format(math.sqrt(num)));
print("Arredondamento para cima : {}".format(math.ceil(num)));
print("Arredondamento para baixo : {}".format(math.floor(num)));
print("Parte inteira : {}".format(math.trunc(num)))

#Exercício 7
palavra = input("Digite uma palavra: ");
cont = 0;
for letra in palavra : 
    print(letra.upper()); #imprime letra a letra
    #Verifico quantas vogais existem na palavra
    vogais = "aeiouAEIOU";
    if letra in vogais:
        cont += 1;
print("A palavra {} possui {} vogais".format(palavra,cont));
#Verifico se a palavra tem a letra A
palavra.find("A");
if palavra.find("A") != -1:
    print("A palavra {} possui a letra A".format(palavra));
else:
    print("A palavra {} não possui a letra A".format(palavra));

#jeito alternativo de printar letra a letra(achei menos prático pro exercício)
#for c in range(len(palavra)):
    #print(palavra[c]);


#Exercício 8
num1 = float(input("Digite o primeiro número: "));
num2 = float(input("Digite o segundo número: "));

print("A soma de {} + {} = {}".format(num1,num2,num1+num2));
print("A subtração de {} - {} = {}".format(num1,num2,num1-num2));
print("A multiplicação de {} x {} = {}".format(num1,num2,num1*num2));
print("A divisão de {} / {} = {}".format(num1,num2,num1/num2));
print("O resto da divisão de {} % {} = {}".format(num1,num2,num1%num2));
print("A potência de {} ^ {} = {}".format(num1,num2,num1**num2));



