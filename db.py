import psycopg2
from contextlib import contextmanager

parametros = dict(
    host='localhost', 
    database='Python',
    user='postgres', 
    password='postgres')

@contextmanager
def nova_conexao():
    conexao = psycopg2.connect(**parametros)
    try:
        yield conexao
    finally:
        if(conexao and conexao.isexecuting()):
            conexao.close()
        print("Finally")
