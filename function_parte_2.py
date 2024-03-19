'''Parametros especiais
Por padrão, argumentos podem ser passados para uma função python tanto po posição
quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido
restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa
apenas olhar para a definição da função para determinar se os itens são passados
por posição, por posição e nome, ou por nome'''

#positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor="1.0",
combustivel="Gasolina")#válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido

#keyword only
def criar_carro(*, modelo, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor="1.0",
combustivel="Gasolina")

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#keyword and positional only

def criar_carro(modelo, ano, plca, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor="1.0",
combustivel="Gasolina")

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

'''Objetos de primeira classe
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe.
Com isso podemos atribuir funções a variáveis, passá-las como parâmetros para funções, usá-las como valores
em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para função (closures)
'''

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

'''Escopo local e escopo gloal
Python trabalha com escopo local e global, dentro do bloco da 
função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser
execuado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a
variável que está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser evitada'''

salario = 2000
def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)

