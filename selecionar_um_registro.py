import psycopg2

def conecta_DB():
    try:
        conexao = psycopg2.connect(
            host = 'localhost', 
            database = 'Python', 
            user = 'postgres',
            password = 'postgres')
    except psycopg2.ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print('Banco conectado!')
        return conexao

if __name__=='__main__':
    try:
        conexao = conecta_DB()
        sql = '''select nome, telefone from contatos 
                 offset 2'''
        cursor = conexao.cursor()
        cursor.execute(sql)
    except psycopg2.ProgrammingError as e:
        print(f'Erro: {e}')
    else:
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
            print(f'registro:{cursor.fetchone()}')
    conexao.close()