import psycopg2

def conecta_DB():
    try:
        conexao = psycopg2.connect(user = 'postgres',
                                   database = 'Python',
                                   password = 'Genius2003$',
                                   host = 'localhost')
    except psycopg2.ProgrammingError as erro:
        print('Erro:'+ erro)
    else:
        print(f'Banco de dados conectado')       
        return conexao         
def criarTabela_grupo():
    sql = '''create table if not exists grupo(
         id serial primary key,
         descricao varchar(30))'''
    cursor.execute(sql)
# comandos DDL o commit está implicito    

def alterarTabela_contatos():
    sql = '''alter table contatos 
             add column grupo_id integer'''
    #cursor.execute(sql)
    sql1 = '''alter table contatos 
             add foreign key (grupo_id)
             references grupo(id)'''
    cursor.execute(sql1)

def inserirDados_tabela_Grupo():
    sql = '''insert into grupo (descricao) values (%s)'''
             
    args = (('Casa',),
           ('Trabalho',),)   
    cursor.executemany(sql,args)
    conexao.commit()


if __name__=='__main__':
    conexao = conecta_DB()
    cursor = conexao.cursor()
    criarTabela_grupo()
    alterarTabela_contatos()
    inserirDados_tabela_Grupo()
    conexao.close()
