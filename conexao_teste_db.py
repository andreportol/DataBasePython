from db import nova_conexao

with nova_conexao() as conexao:
    if conexao.isexecuting():
        print('Conectado!')
print('fim')