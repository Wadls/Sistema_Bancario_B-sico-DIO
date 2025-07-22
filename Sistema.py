
operacoes_bancarias = []
conta = 1000
saque_diario = 3
LIMITE_SAQUE = 500
def extrato():
    i = 0
    for index in operacoes_bancarias:
        i+=1
        if index > 0:
            print(f'- Operação {i}, depósito de R${index:.2f} ')
        else:
            print(f'- Operação {i}, saque de -R${(index*-1):.2f} ')
    if not operacoes_bancarias:
        print('Lista Vazia')
    
             
def deposito(valor):
    operacoes_bancarias.append(valor)
   
def saque(valor):
    operacoes_bancarias.append(valor*-1)
    
menu = '''\n
=========== MENU ===========
[D] Depósito
[S] Saque
[E] Extrato
[B] Saída
============================
\n\n'''

while True:
    switch = input(menu)
    if switch.lower() == 'd':
        deposito(int(input('\n Defina o valor de depósito: ')))
    elif switch.lower() == 's':
        saque_diario-=1
        if saque_diario >= 0 :
            valor_saque = int(input('informe o valor do saque: '))

            if saque_diario >= 0 and valor_saque <= 500:
                if (conta-valor_saque) >= 0:
                    saque(valor_saque)
                    conta -= valor_saque
                else:
                    print(f'\nSaldo Insuficiente')
            elif valor_saque > 500:
                print('\n Valor Máximo de Saque Atingido')
        elif saque_diario < 0:
                print('\nLimite de Saques Diários Atingidos')
            
        else:
            continue

    elif switch.lower() == 'e':
        extrato()
        print(f'\n Valor Atual em conta: {conta}')
    elif switch.lower() == 'b':
        break
    else:
        print('Entrada Não Reconhecida')
        
