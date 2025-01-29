from BancoDados import get_connection, close_connection, list_schemas
import streamlit as st


conn = get_connection()

Segmento = list(list_schemas(conn))
print(Segmento) 

if conn:
    close_connection(conn)


st.selectbox('Escolha o segmento' + Segmento)