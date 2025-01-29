from BancoDados import get_connection, close_connection, list_schemas, get_sales_data
import streamlit as st


conn = get_connection()

Segmento = list(list_schemas(conn))


st.title("📊 Dashboard Empresarial")

# Selectbox para o usuário escolher um segmento
if Segmento:
    segmento_escolhido = st.selectbox('Escolha o segmento:', Segmento)

    dados = get_sales_data(segmento_escolhido)

    # Exibir os dados se houver resultado
    if not dados.empty:
        st.write(f"📈 Receita total por data para o schema: **{segmento_escolhido}**")
        st.bar_chart(dados.set_index("data_venda"))  # Usa "data_venda" como eixo X
    else:
        st.warning("Nenhum dado encontrado para esse schema.")
else:
    st.error("Nenhum schema encontrado no banco.")