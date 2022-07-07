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

sql = ''' insert into contatos (nome, telefone)
          values (%s,%s)'''
args = ('André', '999391551')

conexao = conexao_DB()
cursor = conexao.cursor()
cursor.execute(sql,args)
conexao.commit()
print('1 registro incluido, ID: ', cursor.lastrowid)
conexao.close()