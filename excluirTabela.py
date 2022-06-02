from requerimentos import conecta_db

sql = 'Drop table if exists emails'

if __name__=='__main__':
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit() # salva no banco de dados
    conexao.close() # fecha conexao