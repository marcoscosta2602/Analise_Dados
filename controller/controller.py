import pandas as pd
import streamlit as st
from model.database import run_query
from model.queries import QUERIES


def get_segment_data(segmento):
    """Busca dados do segmento no banco."""
    if segmento in QUERIES:
        return run_query(QUERIES[segmento])
    return None

def prepare_data(df):
    """Padroniza e converte os dados para evitar erros nos gráficos"""
    if df is None or df.empty:
        return df  # Retorna vazio se os dados não existirem
    
    # Normaliza os nomes das colunas para minúsculas
    df.columns = [col.lower() for col in df.columns]

    # Converte colunas para os tipos corretos
    if "data_venda" in df:
        df["data_venda"] = pd.to_datetime(df["data_venda"])  # Converter para data

    if "total_receita" in df:
        df["total_receita"] = pd.to_numeric(df["total_receita"], errors="coerce")  # Converter para número

    if "quantidade_vendas" in df:
        df["quantidade_vendas"] = pd.to_numeric(df["quantidade_vendas"], errors="coerce")  # Converter para número

    return df
