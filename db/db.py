import os
import psycopg2

# Carrega variável de ambiente com string de conexão do banco:
database_url = os.getenv('DATABASE_URL')

#Funções realizam conexão com banco, utilizando dicionário contendo parâmetros de conexão, retornado da função config(), do arquivo config.py, assim realizando uma consulta e então fechando a conexão.

def cadastraAluno(nome, matricula):
    conn = None
    try:
        # Conexão com banco:
        conn = psycopg2.connect(database_url)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere aluno, utilizando argumentos da função:
        cur.execute('INSERT INTO aluno (nome, matricula) VALUES (%s, %s)', (nome, matricula))

        print("foi")

        #Confirma transação:
        conn.commit()
        print("Aluno cadastrado!")

        cur.close()

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def getAlunos():
    conn = None
    try:
        # Conexão com banco:
        conn = psycopg2.connect(database_url)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere aluno, utilizando argumentos da função:
        cur.execute('SELECT nome, matricula FROM aluno')
        alunos = cur.fetchall()

        #Confirma transação:
        conn.commit()

        cur.close()

        return alunos

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")
    
def addDisciplina(nome):
    conn = None
    try:
        # Conexão com banco:
        conn = psycopg2.connect(database_url)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere disciplina, utilizando argumentos da função:
        cur.execute('INSERT INTO disciplina (nome) VALUES (%s)', (nome))
        
        #Confirma transação:
        conn.commit()
        print("Disciplina adicionada!")

        cur.close()
        

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def getDisciplinas():
    conn = None
    try:

        # Conexão com banco:
        conn = psycopg2.connect(database_url)

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

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")

def addAvaliacao(matricula, nome_disciplina, nota1, nota2, data_avaliacao):
    conn = None
    try:

        # Conexão com banco:
        conn = psycopg2.connect(database_url)

        #Permite executar comandos SQL na sessão atual:
        cur = conn.cursor()

        #Insere avaliação, utilizando argumentos da função:
        cur.execute('CALL addAvaliacao(%s, %s, %s, %s, %s)', (matricula, nome_disciplina, nota1, nota2, data_avaliacao))
        
        #Confirma transação:
        conn.commit()
        print("Avaliação adicionada!")

        cur.close()
        

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexão com banco finalizada.")
