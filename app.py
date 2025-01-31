import streamlit as st
from controller.controller import get_segment_data
from view.charts import VarejoDashboard, SaúdeDashboard, TecnologiaDashboard
from model.queries import QUERIES

 # 📌 Criar navegação na barra lateral
st.sidebar.header("📌 Escolha o Segmento")
segmento = st.sidebar.selectbox("Segmento:", list(QUERIES.keys()))

with st.container():
  
    # Buscar os dados do segmento
    dados = get_segment_data(segmento)


    if dados is not None and not dados.empty:
        if segmento == "Varejo":
            dashboard = VarejoDashboard(dados)
            dashboard.exibir_graficos()

        elif segmento == "Saúde":
            dashboard = SaúdeDashboard(dados)
            dashboard.exibir_graficos()

        elif segmento == "Tecnologia":
            dashboard = TecnologiaDashboard(dados)
            dashboard.exibir_graficos()

    else:
        st.warning(f"Nenhum dado encontrado para {segmento}.")




