from model.database import get_connection

QUERIES = {
    "Varejo": """
    Select v.data_venda, p.categoria, p.nome_produto, SUM(v.receita) as total_receita 
    FROM "AnaliseDados"."Varejo".vendas as v 
    join "Varejo".produtos p on p.id_produto = v.id_produto 
    GROUP BY v.data_venda, p.categoria, v.receita, p.nome_produto
    ORDER BY v.data_venda
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