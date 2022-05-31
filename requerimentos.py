import psycopg2

# Função para criar conexão no banco
def conecta_db():
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
# Função para criar tabela no banco
def criar_db(sql):
  conexao = conecta_db()
  cursor = conexao.cursor()
  cursor.execute(sql)
  conexao.commit()
  conexao.close()

# Listar banco de dados
def listar_db(sql):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(sql)
                                        # i = 1, i começa com 1
    for i, database in enumerate(cursor,start = 1):
        print(f'Banco de dados {i} : {database[0]}')


if __name__=='__main__':
    
    sql = '''CREATE TABLE if not exists deputados 
      ( id            character varying(10), 
        uri           character varying(100), 
        nome          character varying(500), 
        siglaPartido  character varying(50), 
        uriPartido    character varying(200), 
        siglaUf       character varying(10), 
        idLegislatura character varying(10), 
        urlFoto       character varying(100), 
        email         character varying(100) 
      )'''
  
    sq1 = '''SELECT datname FROM pg_database'''
    #criar_db(sq1)
    listar_db(sq1)
