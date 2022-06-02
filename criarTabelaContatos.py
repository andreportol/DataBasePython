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

if __name__=='__main__':
    tabela_contatos = ''' create table contatos
        (nome varchar(50),
        telefone varchar(40))'''

    tabela_emails = '''create table emails
        (id int primary key,
        dono varchar(50))''' 

    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(tabela_contatos)
    cursor.execute(tabela_emails)
    conexao.commit()
    conexao.close()

