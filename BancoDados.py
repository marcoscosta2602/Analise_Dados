import psycopg2
from psycopg2 import sql

def get_connection():
    """
    Cria e retorna uma conexão com o banco de dados PostgreSQL.
    Certifique-se de substituir os valores de host, database, user e password.
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="AnaliseDados",
            user="postgres",
            password="Sistemas2029",
            port=5432
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def close_connection(conn):
    """Fecha a conexão com o banco de dados."""
    if conn:
        conn.close()

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Conexão bem-sucedida!")
        close_connection(conn)
