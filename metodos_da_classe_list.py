lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # 1, "Python", []


lista2 = [1, "Python", [40, 30, 20]]

lista.copy()
print(lista2) # [1, "Python", [40, 30, 20]]


cores = ["Vermelho", "Azul", "Verde", "Azul"]

cores.count("Vermelho") #1
cores.count("Azul") #2
cores.count("Verde") #1



linguagens = ["Python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"]) # vai acrescentar esses dois para a lista
print(linguagens)

#Usamos o index para visualizar qual posição da lista está sendo usada
lingagens2 = ["Python", "js", "c", "java", "csharp"]

lingagens2.index("java")
linguagens2.index("python")

#funcionamento como de uma pilha first in last out
lingagens3 = ["Python", "js", "c", "java", "csharp"]
lingagens3.pop() #csharp
lingagens3.pop() # java
lingagens3.pop() # c
lingagens3.pop(0) #python


# Vai remover C da lista
linguagens4 = ["Python", "js", "c", "java", "csharp"]

linguagens4.remove("c")

#O reverse faz a transposição da lista
linguagens5 = ["Python", "js", "c", "java", "csharp"]

linguagens5.reverse()
print(linguagens5) # csharp, java, c, js, python


linguagens6 = ["Python", "js", "c", "java", "csharp"]
linguagens6.sort() # c, csharp, java, js, python


linguagens6 = ["Python", "js", "c", "java", "csharp"]
linguagens6.sort(reverse=True) # Python, js, java, csharp, c


linguagens6 = ["Python", "js", "c", "java", "csharp"]
linguagens6.sort(key=lambda x: len(x)) # c, js, java, python, csharp


linguagens6 = ["Python", "js", "c", "java", "csharp"]
linguagens6.sort(key=lambda x: len(x), reverse=True) # Python, csharp, java, js, c

#vai fazer a contagem da lista
lingagens7 = ["Python", "js", "c", "java", "csharp"]
len(lingagens7)


linguagens8 = ["Python", "js", "c", "java", "csharp"]
sorted(linguagens8, key=lambda x: len(x)) # c, js, java, python

sorted(linguagens8, key=lambda x: len(x), reverse=True) # python, csharp, java, js, c