import streamlit as st
from controller.controller import get_segment_data
from view.charts import varejo_chart, saude_chart, tecnologia_chart
from model.queries import QUERIES


st.title("📊 Dashboard Empresarial")


# Selectbox para o usuário escolher um segmento
segmento = st.selectbox('Escolha o segmento:', list(QUERIES.keys()))

dados = get_segment_data(segmento)

if dados is not None and not dados.empty:
    if segmento == "Varejo":
        varejo_chart(dados)
    elif segmento == "Saúde":
        saude_chart(dados)
    elif segmento == "Tecnologia":
        tecnologia_chart(dados)
else:
    st.warning(f"Nenhum dado encontrado para {segmento}.")