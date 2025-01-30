from model.database import get_connection
QUERIES = {
    "Varejo": """
        SELECT data_venda, SUM(receita) AS total_receita
        FROM "AnaliseDados"."Varejo".vendas
        GROUP BY data_venda
        ORDER BY data_venda;
    """,
    "Saúde": """
        SELECT data_consulta AS data_venda, SUM(valor_consulta) AS total_receita
        FROM "AnaliseDados"."Saúde".consultas
        GROUP BY data_consulta
        ORDER BY data_consulta;
    """,
    "Tecnologia": """
        SELECT data_pedido AS data_venda, SUM(valor) AS total_receita
        FROM "AnaliseDados"."Tecnologia".pedidos
        GROUP BY data_pedido
        ORDER BY data_pedido;
    """
}