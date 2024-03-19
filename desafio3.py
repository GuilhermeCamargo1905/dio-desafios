import re
def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
    for caractere in senha:
        if caractere.isupper():
            tem_letra_maiuscula = True
        elif caractere.islower():
            tem_letra_minuscula = True
    if not tem_letra_maiuscula or not tem_letra_minuscula:
        return "Sua senha deve conter pelo menos uma letra maiuscula e uma letra minuscula."
    if not any(caractere.isdigit() for caractere in senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    return "Sua senha atende aos requisitos de seguranca. Parabens!"

senha = input().strip()

resultado = verificar_forca_senha(senha)
print(resultado)