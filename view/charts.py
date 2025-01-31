import plotly.express as px
import streamlit as st
import orjson as oj
import uuid  


# 🔹 Configuração da página
st.set_page_config(layout="wide")


class VarejoDashboard:
    def __init__(self, dados):
        self.dados = dados

    def total_vendas_chart(self):
        fig = px.bar(self.dados, x="data_venda", y="quantidade_vendas", title="📈 Vendas Totais - Por Dia", height=500)
        fig.add_hline(y=3, line_dash="dash", line_color="red", annotation_text=f"Meta: {3}", 
                  annotation_position="top left", annotation_font_size=12   )
        fig.update_layout(showlegend=False, title_x=0.34)
        return fig

    def total_receita_chart(self):
        fig = px.line(self.dados, x="data_venda", y="total_receita", title="💰 Receita Total - Por Dia", markers=True, height=500)
        fig.add_hline(y=2800, line_dash="dash", line_color="red", annotation_text=f"Meta: {2800}", 
                  annotation_position="top left", annotation_font_size=12   )
        fig.update_layout(showlegend=False, title_x=0.34)
        return fig

    def receita_por_categoria_chart(self):
        fig = px.pie(self.dados, values="total_receita", names="categoria", title="📈 Receita por Categoria", height=500)
        fig.update_layout(showlegend=True, title_x=0.34)
        return fig

    def receita_por_produto_chart(self):
        fig = px.pie(self.dados, values="total_receita", names="nome_produto", title="📈 Receita por Produto", height=500)
        fig.update_layout(showlegend=True, title_x=0.34)
        return fig
    
    def exibir_cartoes_resumo(self):
        """Exibe cartões com os totais de vendas, receita bruta, ROI e receita líquida"""
        if self.dados is None or self.dados.empty:
            st.warning("⚠️ Nenhum dado disponível para exibir métricas.")
            return

        total_vendas = int(self.dados["quantidade_vendas"].sum())
        receita_bruta = float(self.dados["total_receita"].sum())
        custo_total = receita_bruta * 0.65  # Simulando um custo (ajuste conforme necessário)
        receita_liquida = receita_bruta - custo_total
        roi = ((receita_bruta - custo_total) / custo_total) * 100 if custo_total > 0 else 0

        # Layout dos cartões em uma única linha ocupando toda a largura
        with st.container():
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown('<div class="card">🛍️ Total de Vendas<br><span class="big-metric">{:,}</span></div>'.format(total_vendas), unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="card">💰 Receita Bruta<br><span class="big-metric">R$ {:,.2f}</span></div>'.format(receita_bruta), unsafe_allow_html=True)

            with col3:
                st.markdown('<div class="card">📈 ROI (%)<br><span class="big-metric">{:.2f}%</span></div>'.format(roi), unsafe_allow_html=True)

            with col4:
                st.markdown('<div class="card">💵 Receita Líquida<br><span class="big-metric">R$ {:,.2f}</span></div>'.format(receita_liquida), unsafe_allow_html=True)



    def exibir_graficos(self):
        """Exibe os gráficos dentro de containers estilizados com bordas"""
        if self.dados is not None and not self.dados.empty:
            
            st.markdown("""
                <h2 style="text-align: center;">📊 Visão Geral do Segmento Varejo</h2><BR>
            """, unsafe_allow_html=True)
            
            with st.container():
                col1, col2 = st.columns(2)

                with col1:
                    fig_vendas = self.exibir_cartoes_resumo()
                    if fig_vendas:
                        st.plotly_chart(fig_vendas, use_container_width=True)
                    else:
                        st.warning("⚠️ Nenhum dado disponível para o gráfico de vendas.")

            
                col1, col2 = st.columns(2)

                with col1:
                    with st.container(border=True):
                        st.markdown('<div class="grafico-container">', unsafe_allow_html=True)
                        st.plotly_chart(self.total_vendas_chart(), use_container_width=True, key=f"vendas_{uuid.uuid4()}")
                        st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    with st.container(border=True):
                        st.markdown('<div class="grafico-container">', unsafe_allow_html=True)
                        st.plotly_chart(self.total_receita_chart(), use_container_width=True, key=f"receita_{uuid.uuid4()}")
                        st.markdown('</div>', unsafe_allow_html=True)

            with st.container():
                col1, col2 = st.columns(2)

                with col1:
                    with st.container(border=True):
                        st.markdown('<div class="grafico-container">', unsafe_allow_html=True)
                        st.plotly_chart(self.receita_por_categoria_chart(), use_container_width=True, key=f"categoria_{uuid.uuid4()}")
                        st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    with st.container(border=True):
                        st.markdown('<div class="grafico-container">', unsafe_allow_html=True)
                        st.plotly_chart(self.receita_por_produto_chart(), use_container_width=True, key=f"produto_{uuid.uuid4()}")
                        st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.warning("⚠️ Nenhum dado encontrado para Varejo.")

class SaúdeDashboard:
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

class TecnologiaDashboard:   
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
