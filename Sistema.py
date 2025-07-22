'''def saque():
    b='32'''

operacoes_bancarias = [45]

def extrato():
    i = 0
    for index in operacoes_bancarias:
        i+=1
        if index > 0:
            print(f'- Operação {i}, depósito de R${index:.2f} ')
        else:
            print(f'- Operação {i}, saque de R${index:.2f} ')
            
       

def deposito():
   a = 32 

menu = '''
=========== MENU ===========
[D] Depósito
[S] Saque
[E] Extrato
[S] Saída
============================
'''
while True:
    input(menu)