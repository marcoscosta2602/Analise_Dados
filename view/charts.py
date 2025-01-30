import plotly.express as px
import streamlit as st
import orjson as oj

def varejo_chart(df):
    """Gráficos exclusivos para o segmento Varejo."""
    st.subheader("📈 Receita Total - Varejo")
    fig = px.bar(df, x="data_venda", y="total_receita", text_auto=True,
                 labels={"data_venda": "Data", "total_receita": "Receita"})
    st.plotly_chart(fig)

 # 📈 Gráfico de Linhas - Evolução da Receita
    st.subheader("📊 Evolução da Receita ao Longo do Tempo")
    fig_linhas = px.line(df, x="data_venda", y="total_receita", title="Evolução da Receita")
    st.plotly_chart(fig_linhas)

# 🎂 Gráfico de Pizza - Distribuição da Receita por Categoria
    st.subheader("📊 Distribuição da Receita por Categoria")
    fig_pizza = px.pie(df, values="total_receita", names="categoria", title="Receita por Categoria")
    st.plotly_chart(fig_pizza)

 # 🎂 Gráfico de Pizza - Distribuição da Receita por Categoria
    st.subheader("📊 Distribuição da Receita por Produto")
    fig_pizza = px.pie(df, values="total_receita", names="nome_produto", title="Receita por Categoria")
    st.plotly_chart(fig_pizza)


def saude_chart(df):
    """Gráficos exclusivos para o segmento Saúde."""
    st.subheader("🏥 Consultas e Receita - Saúde")
    
    fig1 = px.line(df, x="data_venda", y="total_receita",
                   labels={"data_venda": "Data", "total_receita": "Receita Total"},
                   title="Evolução da Receita")
    st.plotly_chart(fig1)

    fig2 = px.bar(df, x="data_venda", y="total_consultas", text_auto=True,
                  labels={"data_venda": "Data", "total_consultas": "Número de Consultas"},
                  title="Número de Consultas por Dia")
    st.plotly_chart(fig2)

def tecnologia_chart(df):
    """Gráficos exclusivos para o segmento Tecnologia."""
    st.subheader("💻 Pedidos e Receita - Tecnologia")
    
    fig1 = px.scatter(df, x="data_venda", y="total_pedidos",
                      labels={"data_venda": "Data", "total_pedidos": "Número de Pedidos"},
                      title="Pedidos por Data", size="total_pedidos")
    st.plotly_chart(fig1)

    fig2 = px.line(df, x="data_venda", y="total_receita",
                   labels={"data_venda": "Data", "total_receita": "Receita Total"},
                   title="Receita Total - Tecnologia")
    st.plotly_chart(fig2)
