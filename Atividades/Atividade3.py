#Exercício 1
times = ["Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern de Munique"]
print("Primeiro colocado :  {} , segundo colocado : {} , terceiro colocado : {}".format(times[0], times[1], times[2]))
print("Últimos colocados : {}, {}".format(times[3], times[4]))

# deixando em ordem alfabética
times_alf = tuple(sorted(times))
print(times_alf)

position_barcelona = times.index("Barcelona")
print("Posição de Barcelona na tupla : {}".format(position_barcelona))
