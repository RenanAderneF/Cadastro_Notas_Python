import psycopg2 as p2
from config import config

def connect():
    
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Consulta versão do banco e a exibe:
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")


# Caso esse arquivo .py seja compilado, a função connect() será executada:
if __name__ == '__main__':
    connect()

