import psycopg2

def conexao_DB():
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


sql = '''insert into contatos(nome,telefone) 
        values (%s, %s)'''

args = (('Thaisa', '9993915478'),
        ('Lavinia', '963214765'),
        ('Rebeca', '874521323'),
        ('Eliane', '7887845415'),
        ('Luis', '132165461'))

conexao = conexao_DB()
cursor = conexao.cursor()
cursor.executemany(sql,args)
conexao.commit()
print(f'Foram incluidos {cursor.rowcount} registros.')
conexao.close()
