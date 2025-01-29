from BancoDados import get_connection, close_connection

conn = get_connection()
if conn:
    close_connection(conn)

