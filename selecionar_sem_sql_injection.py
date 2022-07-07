import psycopg2

def conexao_DB():
    try:
        conexao = psycopg2.connect(host='localhost', 
                            database='Python',
                            user='postgres', 
                            password='Genius2003$')
    except psycopg2.OperationalError:
        print('Banco não conectado!')
    else:
        print('Banco de dados conectado!')
        return conexao

conexao = conexao_DB()
cursor = conexao.cursor()
nome = input('Contato a localizar: ')
args = (f'%%{nome}%%',)
sql = '''select * from contatos
        where nome like %s or telefone like '%%1551%%' '''
# like é igual a contido
cursor.execute(sql,args)
for x in cursor:
    print(x)

