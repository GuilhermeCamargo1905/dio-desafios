'''Função é um bloco de codigo identificado por um nome e pode receber uma lista
de paramentros, esses parametros podem ou não ter valores padrões. Usar funções
torna o código mais legível e possibilita o reaptoveitamento de código.
programar baseado em funções é o mesmo que dizer que estamos programando de maneira
estruturada'''

#Exemplo
def exibir_mensagem():
    print('Olá mundo')

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome ="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome = "Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Gustavo")


'''Para retornar um valor utilziamos a plabra reservada return
Toda função python retorna None por padrão
Diferente de outras linguagens de programação, em python uma função pode retornar mais de um valor'''

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

print(func_3())

#Argumentos nomeados são funções também podem ser chamadas usando argumentos nomeados da forma chave=valor
#quando colocamos um dicionario apra a função utilizando **

'''Args e Kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos
(*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in
kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beutiful is better than ugly.", autor = "Tim Peters", ano = 1999)