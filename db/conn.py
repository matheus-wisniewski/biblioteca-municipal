import psycopg2

class DBConnect:
    cursor = ''
    conn = ''

    credenciais = {
        'hostname': 'localhost',
        'user': 'root',
        'senha': '',
        'db': 'usuarios',
        'port': 3306,
    }

    def conn(self):
        conn = psycopg2.connect(database=self.credenciais["hostname"], user=self.credenciais["user"], password=self.self.credenciais["senha"], dbname=self.credenciais["db"], port=self.credenciais["porta"])
        
        self.cursor = conn.cursor()
        self.conn = conn

        pass

    def set_cursor(self, conn):
        self.cursor = conn.cursor()

    def get_cursor(self):
        return self.cursor
    
    def get_conn(self):
        return self.conn