from model.database import get_connection, run_query 
import streamlit as st
import plotly.express as px
import orjson as oj
from model.queries import QUERIES
from model.database import run_query


conn = get_connection()

##Segmento = list(list_schemas(conn))


st.title("📊 Dashboard Empresarial")

# Selectbox para o usuário escolher um segmento

segmento = st.selectbox('Escolha o segmento:', list(QUERIES.keys()))

if segmento in QUERIES:
    dados = run_query(QUERIES[segmento])

    if not dados.empty:
        st.subheader(f"📈 Análise de {segmento}")

        # Gráfico de barras
        fig_bar = px.bar(dados, x="data_venda", y="total_receita",
                         labels={"data_venda": "Data", "total_receita": "Receita"},
                         title=f"Receita Total - {segmento}",
                         text_auto=True)
        st.plotly_chart(fig_bar)

        # Gráfico de linha
        fig_line = px.line(dados, x="data_venda", y="total_receita",
                           labels={"data_venda": "Data", "total_receita": "Receita"},
                           title=f"Evolução da Receita - {segmento}")
        st.plotly_chart(fig_line)

    else:
        st.warning(f"Nenhum dado encontrado para {segmento}.")
