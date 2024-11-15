import psycopg2
from psycopg2 import OperationalError

credenciais = {
    'hostname': 'postgres.railway.internal',
    'user': 'postgres',
    'password': 'mjdFnZrxSxsLIavWgBfyijxOnWEytXBY',
    'db': 'railway',
    'port': 5432,
}

def cria_conexao():
    print("Tentando conectar ao banco...")
    try:
        conn = psycopg2.connect(
            database=credenciais['db']
            ,user=credenciais['user']
            ,password=credenciais['password']
            ,host=credenciais['hostname']
            ,port=credenciais['port']
            )
        return conn
        print("Conexão bem-sucedida ao banco.")
    except OperationalError as e:
        print(f"Erro ao conectar-se ao DB: {e}")


def cria_tabela(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                ano INT NOT NULL,
                editora VARCHAR(100) NOT NULL,
                genero VARCHAR(100) NOT NULL
            );
            """)
            conn.commit()
            print("Tabela 'livros' criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

if __name__ == "__main__":
    conn = cria_conexao()
    if conn:
        cria_tabela(conn)
        conn.close()