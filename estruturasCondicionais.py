MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Maior de idade, pode tirar CNH.')
else:
    print('Ainda não pode tirar a CNH.')



if idade >= 18:
    print('Maior de idade, pode tirar CNH.')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas')
else:
    print('Ainda não pode tirar a CNH.')