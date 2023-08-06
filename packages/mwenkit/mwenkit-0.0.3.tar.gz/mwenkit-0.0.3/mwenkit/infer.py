import pandas as pd

def get_contingency_table(rows, col):
    """
    Params rows  = [data.colx_name...]
           col = [data.colz_name]
    """
    return pd.crosstab(rows, col)