from BancoDados import get_connection, close_connection, list_schemas, get_sales_data, check_table_exists
import streamlit as st
import plotly.express as px


conn = get_connection()

Segmento = list(list_schemas(conn))


st.title("📊 Dashboard Empresarial")

# Selectbox para o usuário escolher um segmento
if Segmento:
    segmento_escolhido = st.selectbox('Escolha o segmento:', Segmento)

    if segmento_escolhido:  
        if check_table_exists(segmento_escolhido):
            dados = get_sales_data(segmento_escolhido)

    # Exibir os dados se houver resultado
            if not dados.empty:
             st.write(f"📈 Receita total por data para o schema: **{segmento_escolhido}**")


             # 📊 Gráfico de Barras - Receita por Data
            st.subheader("Receita Total por Data")
            st.bar_chart(dados.set_index("data_venda")["total_receita"])

             # 📈 Gráfico de Linhas - Evolução da Receita
            st.subheader("Evolução da Receita ao Longo do Tempo")
            fig_linhas = px.line(dados, x="data_venda", y="total_receita", title="Evolução da Receita")
            st.plotly_chart(fig_linhas)

            # 🎂 Gráfico de Pizza - Distribuição da Receita por Categoria
            st.subheader("Distribuição da Receita por Categoria")
            fig_pizza = px.pie(dados, values="total_receita", names="categoria", title="Receita por Categoria")
            st.plotly_chart(fig_pizza)

        else:
            st.warning("Nenhum dado encontrado para esse segmento.")
    else:
        st.error(f"A tabela 'vendas' não existe no segmento '{segmento_escolhido}'.")
else:
    st.error("Nenhum segmento encontrado no banco.")