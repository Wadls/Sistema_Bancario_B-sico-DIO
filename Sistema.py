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
   
def saque(*,saldo, saque_diario, Limite_Saque, Conta):
    if saque_diario > 0 and saldo <= Limite_Saque and Conta-saldo > 0:
        operacoes_bancarias.append(saldo*-1) #Oque torna um saque diferente de um depósito é o seu valor negativo
        return True
    else:
        return False

    
menu = '''\n
=========== MENU ===========
[D] Depósito
[S] Saque
[E] Extrato
[B] Saída
============================
\n\n'''

operacoes_bancarias = []
conta = 1000
saque_diario = 3
LIMITE_SAQUE = 500

while True:
    switch = input(menu)
    if switch.lower() == 'd':
        deposito(int(input('\n Defina o valor de depósito: ')))
    
    elif switch.lower() == 's': #Operações de saque
        valor_saque = float(input('Informe o Valor do Saque:' ))
        realizar_saque = saque(saldo=valor_saque, saque_diario= saque_diario, Limite_Saque=LIMITE_SAQUE, Conta=conta)
        if realizar_saque == True:
            print('Saque realizado')
            saque_diario-=1
            conta-=valor_saque
        else:
            print('Saque Inválido')

    elif switch.lower() == 'e':
        extrato()
        print(f'\n Valor Atual em conta: {conta}')
    elif switch.lower() == 'b':
        break
    else:
        print('Entrada Não Reconhecida')
        
