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


sql = '''update contatos
         set telefone = 9992520749 
         where id = %s'''
# telefone é integer sem apostrofo
sql1 = ''' update contatos
           set nome = 'Andre Porto'
           where  id = %s '''
# Nome é String com apostrofo

id = input("Digite o id do contato que será atualizado: ")
# a virgula serve para indicar ao interpretador python que se trata de uma tupla
args = (id,)
cursor.execute(sql1, id)
conexao.commit()
conexao.close()
