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
sql = '''insert into contatos(nome,telefone)
         values 
         (%s,%s)'''

args = (
        ('Maycon','98745632'),
        ('Celia','456322632'),
        ('Grazi','874125692'),
        ('Rayane','992245710')
        )
try:
    cursor.executemany(sql,args)
except psycopg2.ProgrammingError as erro:
    print(erro)

else:
    print(f'{cursor.rowcount} registro(s) inserido(s)')
    conexao.commit()

conexao.close()