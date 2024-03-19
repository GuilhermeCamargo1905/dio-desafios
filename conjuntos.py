'''Um set é uma coleção que não possui objetos repetidos
usamos sets para representar conjuntos matematicos ou eliminar
itens duplicados de um objeto iteravel'''

numeros = set([1, 2, 1, 3, 4, 4, 5])
print(numeros)

'''Conjuntos python não suportam indexação e nem fatiamento, caso queira acessar
os seus valores é necessário converter o conjunto para lista'''

numeros = {1, 2, 3, 2}

numero = list(numeros)

print(numero[0])

'''Ás vezes é necessario saber qual é o indece que estamos percorrendo'''

#Metodos da classe set
#{}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

#{}.intersection

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d)

#{}.difference
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.difference(conjunto_d)
conjunto_d.difference(conjunto_c)

#{}.symetric_difference
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.symmetric_difference(conjunto_d)

#{}.issubset
conjunto_e = {1, 2, 3}
conjunto_f = {4, 1, 2, 5, 6, 3}

conjunto_e.issubset(conjunto_f)
conjunto_f.issubset(conjunto_e)

#{}.issupserset
conjunto_e = {1, 2, 3}
conjunto_f = {4, 1, 2, 5, 6, 3}

conjunto_e.issuperset(conjunto_f)
conjunto_f.issuperset(conjunto_e)

#{}.isdisjoint
conjunto_g = {1, 2, 3, 4, 5}
conjunto_h = {6, 7, 8, 9}
conjunto_i = {1, 0}

conjunto_g.isdisjoint(conjunto_h)
conjunto_g.isdisjoint(conjunto_i)

#{}.add
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

#{}.discard
numeros1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros1
numeros1.discard(1)
numeros1.discard(45)
numeros1

#{}.pop
numeros2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros2
numeros2.pop()
numeros2.pop()
numeros2

#{}.remove
numeros3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros3
numeros3.remove(0)
numeros3

#{}.len
numeros4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
len(numeros4)

#{}.in
numeros5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
1 in numeros
10 in numeros