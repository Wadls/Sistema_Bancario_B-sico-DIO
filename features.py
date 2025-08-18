diconario = dict()
def criar_usuario(nome, data_de_nascimento,cpf,endereço):
    diconario[nome] = {data_de_nascimento,cpf,endereço}

criar_usuario('JULIO','12/08/2024','6541325455',42, 'teste',12,131,32,1,132,31,1231,1312)
print(diconario)