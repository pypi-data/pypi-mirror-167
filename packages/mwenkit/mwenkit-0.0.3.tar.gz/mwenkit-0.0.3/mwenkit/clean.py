"""
Author: Reme Ajayi
License: MIT License
Contains functions for understanding missing data sources
"""
import numpy as np
import pandas as pd

def get_cols_with_nulls(df):
    '''
    Returns the column names of columns with null values

            Parameters:
                    df (dataframe): A pandas dataframe

            Returns:
                    nan_cols (list): List of strings
    '''
    nan_cols = [i for i in df.columns if df[i].isnull().any()]
    return nan_cols

def create_sub_df_by_dtype(df, data_type):
    """valid types include 'str' and 'num'"""
    if data_type == 'str':
        sub_df = df.select_dtypes(include=['object'])
    elif data_type == 'num':
        sub_df = df.select_dtypes(include=['float64','int64'])
    else:
        print('Datatype not supported')
    return sub_df

def get_cols_with_empty_strings(df):
    '''
    Returns the column names of columns with empty string counts

            Parameters:
                    df (dataframe): A pandas dataframe with ONLY string columns

            Returns:
                    nan_cols (list): List of strings
    '''
    nan_cols = [i for i in df.columns
    if (not (df[i].str.len() > 0).all()) or (df[i].str.isspace().any())]
    return nan_cols


def print_col_empty_string_count(nan_cols, df):
    """
       Print value_counts of distributions

            Parameters:
                    df (dataframe): A pandas dataframe with ONLY string columns
                    nan_cols(list): A list of strings

            Returns:
                    Void
    """
    for col in nan_cols:
        print(col)
        print('Distriubtion of empty strings')
        print((df[col].str.len() > 0).value_counts())
        print('Distribution of strings with just blanks')
        print((df[col].str.isspace().value_counts()))

def get_cols_with_k_null_percent(df, k):
    "k% expressed as a decimal. e.g. 0.2 for 20% null values"
    nan_cols = [i for i in df.columns if df[i].isnull().sum() > k*len(df)]
    return nan_cols
