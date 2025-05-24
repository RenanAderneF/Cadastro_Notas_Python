from configparser import ConfigParser

#Lê seção de um arquivo de configuração, de forma a retorná-la como dicionário para utilizar os dados como parâmetro de conexão do banco, em conn.py:
def config(filename='db.ini', section='postgresql'):
    
    #Cria parser:
    parser = ConfigParser()
    
    #Lê arquivo de configuração:
    parser.read(filename, encoding='latin-1')


	#Cria dicionário a receber os conjuntos chave-valor do .ini:
    db = {}
    
    #Itera sobre cada conjunto, incluindo-os no dicionário criado:
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    
    else:
        raise Exception(f"Seção {section} não encontrada em {filename}.")
    
    return db 