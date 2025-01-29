from BancoDados import get_connection, close_connection

conn = get_connection()
if conn:
    print("Conexão estabelecida!")
    close_connection(conn)

