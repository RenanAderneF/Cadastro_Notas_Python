import psycopg2 as p2 
from config import config

#Funções realizam conexão com banco, utilizando dicionário contendo parâmetros de conexão, retornado da função config(), do arquivo config.py, assim realizando uma consulta e então fechando a conexão.

def testaConn():
    
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

def cadastraAluno(nome, matricula):
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere aluno, utilizando argumentos da função:
        cur.execute('INSERT INTO aluno (nome, matricula) VALUES (%s, %s)', (nome, matricula))

        #Confirma transação:
        conn.commit()
        print("Aluno cadastrado!")

        cur.close()

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def getAlunos():
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere aluno, utilizando argumentos da função:
        cur.execute('SELECT nome, matricula FROM aluno')
        alunos = cur.fetchall()

        #Confirma transação:
        conn.commit()

        cur.close()

        print(alunos)
        return alunos

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")
    
def addDisciplina(nome):
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere disciplina, utilizando argumentos da função:
        cur.execute('INSERT INTO disciplina (nome) VALUES (%s)', (nome))
        
        #Confirma transação:
        conn.commit()
        print("Disciplina adicionada!")

        cur.close()
        

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def getDisciplinas():
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere aluno, utilizando argumentos da função:
        cur.execute('SELECT nome FROM disciplina')
        disciplinas = cur.fetchall()
        
        #Confirma transação:
        conn.commit()

        cur.close()
        
        print(disciplinas)
        return disciplinas

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def addAvaliacao(matricula, nome_disciplina, nota1, nota2, data_avaliacao):
    conn = None
    try:

        #Recebe dicionário correspondente aos dados de conexão:
        params = config()

        #Realiza conexão com banco utilizando parâmetros recebidos.
        conn = p2.connect(**params)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere avaliação, utilizando argumentos da função:
        cur.execute('CALL addAvaliacao(%s, %s, %s, %s, %s)', (matricula, nome_disciplina, nota1, nota2, data_avaliacao))
        
        #Confirma transação:
        conn.commit()
        print("Avaliação adicionada!")

        cur.close()
        

    except (Exception, p2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")
