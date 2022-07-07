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
sql = '''select * from contatos
        where telefone like '%11%' '''
cursor.execute(sql)
contatos = cursor.fetchall()
for i, contato in enumerate (contatos, start = 1):
    print(f'{i} = {contato[0]},{contato[1]}')
