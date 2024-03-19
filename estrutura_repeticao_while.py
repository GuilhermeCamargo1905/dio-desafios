opcao = -1

while opcao != 0:
    opcao = int(input("[1] SACAR \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato")
    elif opcao == 0:
        print("Fechando o programa")
    else:
        print('Digite um valor dentro das opções')


