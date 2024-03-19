numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#adicionar na lista
numeros2 = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros2 if numero % 2 == 0]

#modificar valores na lista
numeros3 = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros3]