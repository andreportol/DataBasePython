from requerimentos import conecta_db


sql= """SELECT tablename FROM pg_tables
        WHERE schemaname = 'public'  
        ORDER BY tablename;"""

if __name__=='__main__':
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(sql)
    for i, table in enumerate(cursor,start=1):
        print(f'Tabela {i}: {table[0]}')
    conexao.commit()
    conexao.close()