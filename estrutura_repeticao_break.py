
# Também podemos utilizar o continue dentro do while
while True:
    opcao = int(input('Informe um número: '))

    if opcao == 10:
        break

    print(opcao)

# Vai informar os numeros pares
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")