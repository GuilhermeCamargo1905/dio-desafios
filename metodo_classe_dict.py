#{}.clear

contato = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
}

contato.clear()
contato

#{}.copy
contato = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contato.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contato["guilherme@gmail.com"]

copia["guilherme@gmail.com"]

#{}.fromkeys
dict.fromkeys(["nome", "telefone"])

dict.fromkeys(["nome", "telefone"], "vazio")

#{}.get
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos["chave"]

contatos.get("chave")
contatos.get("chave", {})
contatos.get("guilherme@gmail.com", {})

#{}.pop
contatos'{
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com")

contatos.pop("guilherme@gmail.com", "Não encontrou")

#{}popitem
contatos{
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.popitem()

#{}.setdefault
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")
contato

contato.setdefault("idade", 28)
contato


#{}.update
contato = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos

#{}.value = retorna os valores do dicionario

#{}.in podemos verificar se um valor é uma chave dentro de um determinado dicionario

#{}.del vai ser passado um objeto que queremos remover