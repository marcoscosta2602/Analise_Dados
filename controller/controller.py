from model.database import run_query
from model.queries import QUERIES

def get_segment_data(segmento):
    """Busca dados do segmento no banco."""
    if segmento in QUERIES:
        return run_query(QUERIES[segmento])
    return None