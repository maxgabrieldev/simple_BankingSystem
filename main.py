menu = '''      
    Max's Virtual Bank
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=> Escolha uma opção: '''

saldo = 0
limite = 500
extrato = "Extrato: \n"
numero_saques = 0
LIMITE_QUANTIDADE_SAQUE = 3


while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: {valor:.2f} \n'
            print('Depósito realizado com sucesso!')
        else:
            print('Valor inválido!')
            
    elif opcao == 's':
        valor = float(input('Valor do saque: '))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saque = numero_saques >= LIMITE_QUANTIDADE_SAQUE
        
        if excedeu_saldo:
            print('Saldo insuficiente!')
        elif excedeu_limite:
            print('Limite excedido!')
        elif excedeu_saque:
            print('Limite de saques excedido!')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: {valor:.2f} \n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
             
    elif opcao == 'e':
        print('\n========== Extrato ==========')
        print('Não há lançamentos no extrato' if not extrato else extrato)
        print(f'Saldo: {saldo:.2f}')
        print('=============================\n')

    elif opcao == 'q':
        print('Saindo...')
        break
    
    else:
        print('Opção inválida!')