
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iteravel
for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")
    else:
        print() # Adiciona uma quebra de linha

# Exemplo utilizando função range
for numero in range(0, 51, 5):
    print(numero, end="")