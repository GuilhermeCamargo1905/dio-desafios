'''Um dicionário é um conjunto não-ordenado de pares
chave: valor, onde as chaves são únicas em uma dada instância do dicionário.
Dicionários. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:
valor separada por vírgulas'''

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade = 28)

pessoa["telefone"] = "3333-1234"

#acessar valores no dicionario
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "Guilherme"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados

'''dicionarios podem armazenar qualquer tipo de objeto python
comovalor, desde que a chave para esse valor seja um objeto
imutável como (strings e números)'''

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
}

contatos["giovanna@gmail.com"]["telefone"]

'''A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for'''

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)