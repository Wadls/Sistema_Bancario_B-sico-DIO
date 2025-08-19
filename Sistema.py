

def extrato():
    i = 0
    print('''\n
    +=========== EXTRATO ===========+
''')
    for index in operacoes_bancarias:
        i+=1
        if index > 0:
            print(f'- Operação {i}, depósito de R${index:.2f} ')
        else:
            print(f'- Operação {i}, saque de -R${(index*-1):.2f} ')
    if not operacoes_bancarias:
        print('Lista Vazia')
    print('''\n
    +===============================+
''')
               
def deposito(valor):
    operacoes_bancarias.append(valor)
   
def saque(*,saldo, saque_diario, Limite_Saque, Conta):
    if saque_diario > 0 and saldo <= Limite_Saque and Conta-saldo > 0:
        operacoes_bancarias.append(saldo*-1) #Oque torna um saque diferente de um depósito é o seu valor negativo
        return True
    else:
        return False

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    
    for i in contas:
        for j in i.items():
            print(j)



menu = '''\n
=========== MENU ===========
[D]     Depósito
[S]     Saque
[E]     Extrato
[Nc]    Nova Conta
[Nu]    Novo Usuário
[Nl]    Nova Conta
[Lc]    Listar Contas
[B] Saída
============================
\n\n'''
LIMITE_SAQUE = 500
AGENCIA = '0001'

operacoes_bancarias = []
usuarios = []
contas = []
conta = 1000
saque_diario = 3

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
    elif switch.lower() == 'nu':
        criar_usuario(usuarios)    
    elif switch.lower() == 'nc':
        numero_conta = len(contas) + 1
        conta_criada = criar_conta(AGENCIA,numero_conta,usuarios)
        if conta_criada:
            contas.append(conta_criada)
    
    elif switch.lower() == 'lc':
        listar_contas(contas)
    elif switch.lower() == 'b':
        break

    else:
        print('Entrada Não Reconhecida')
        
