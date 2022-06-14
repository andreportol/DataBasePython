import psycopg2
import psycopg2.errors

def conecta_DB():
    try:
        conexao = psycopg2.connect(host='localhost', 
                            database='Python',
                            user='postgres', 
                            password='postgres')
    except psycopg2.OperationalError:
        print('Banco não conectado!')
    else:
        print('Banco de dados conectado!')
        return conexao

sql = '''alter table contatos 
add column id serial primary key'''

conexao = conecta_DB()
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()


    