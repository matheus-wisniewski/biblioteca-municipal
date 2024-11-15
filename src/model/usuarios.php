import sys
import os

sys.path.append(os.path.abspath('../../'))
from db import cria_conexao as db

def get_usuarios():
    conn = db()
    cursor = conn.cursor()

    try:
        sql = 'SELECT * FROM usuarios'
        cursor.execute(sql)
        response = cursor.fetchall()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if conn:
            conn.close()
            print("Conexão encerrada")
    
    return response
    