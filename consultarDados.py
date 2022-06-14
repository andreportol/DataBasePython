import psycopg2

def conectarBD():
    try:
        conexao = psycopg2.connect(host ='localhost',
                                   database = 'Python',
                                   user= 'postgres',
                                   password = 'postgres')
    except psycopg2.ProgrammingError as e:
        print('Banco não conectado!')
    else:
        print('Conectado ao banco')
        return conexao


if __name__=='__main__':
    try:
        conexao = conectarBD()
        cursor = conexao.cursor()
        sql = '''select * from contatos 
                 limit 10
                 offset 20'''
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except psycopg2.ProgrammingError as e:
        print('teste')
        print(f'Erro{e}')    
    else:
        for contato in contatos:
            print(f'id:{contato[2]:3d} Nome:{contato[0]:12s} telefone: {contato[1]:10s}')
    
    conexao.commit()
    conexao.close()