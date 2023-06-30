#Sistema bancário
import os

menu = '''      
    Max's Virtual Bank
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=> Escolha uma opção: '''

saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_QUANTIDADE_SAQUE = 3


while True:
    opcao = input(menu)
    if opcao == 'q':
        print('Saindo...')
        break
    elif opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: '))
        saldo += valor
        extrato.append(['Depósito', valor])
        print('Depósito efetuado com sucesso!')
    elif opcao == 's':
        valor = float(input('Digite o valor a ser sacado: '))
        if valor > saldo:
            print('Saldo insuficiente!')
        elif valor > limite_saque:
            print('Limite de saque excedido!')
        elif numero_saques >= LIMITE_QUANTIDADE_SAQUE:
            print('Limite de saques diários excedido!')
        else:
            saldo -= valor
            limite_saque -= valor
            extrato.append(['Saque', valor])
            numero_saques += 1
            print('Saque efetuado com sucesso!')
    elif opcao == 'e':
        print('Extrato')
        print('=======')
        print('Tipo\tValor')
        for tipo, valor in extrato:
            print(f'{tipo}\t{valor}')
        print('=======')
        print(f'Saldo: {saldo}')
    else:
        print('Opção inválida!')


