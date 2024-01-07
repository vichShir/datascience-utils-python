import pandas as pd
import numpy as np
from sklearn import preprocessing
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

def normalize(dataframe:pd.DataFrame, columns:list=None, by_dtype:list=None, inplace:bool=False):
  """ Normalize columns given a pandas dataframe using MinMaxScaler
  dataframe: Pandas DataFrame
  columns: list of columns
  by_dtype: list of specific dtypes
  inplace: return dataframe
  """

  df = dataframe.copy()
  min_max_scaler = preprocessing.MinMaxScaler()

  if inplace == False:
    # Normalize the given columns
    if columns != None:
      for column in columns:
        df[column] = min_max_scaler.fit_transform(np.array(df[column]).reshape(-1, 1))
    else: # Normalize by dtype
      for column in df.columns:
        if df[column].dtype in by_dtype:
          df[column] = min_max_scaler.fit_transform(np.array(df[column]).reshape(-1, 1))
    return df
  else:
    # Normalize the given columns
    if columns != None:
      for column in columns:
        dataframe[column] = min_max_scaler.fit_transform(np.array(dataframe[column]).reshape(-1, 1))
    else: # Normalize by dtype
      for column in dataframe.columns:
        if dataframe[column].dtype in by_dtype:
          dataframe[column] = min_max_scaler.fit_transform(np.array(dataframe[column]).reshape(-1, 1))


def impute_missing_data(dataframe, columns:list=None, fill_method=np.nanmedian, inplace=False):
  """ Fill missing data
  dataframe: Pandas DataFrame
  columns: list of columns
  fill_method: numpy method for numerical columns
  inplace: return dataframe
  """

  df = dataframe.copy()

  if inplace == False:
    for column in columns:
      if is_numeric_dtype(df[column]):
        col_stats = fill_method(df[column]) # mean, median, mode...
        df[column] = df[column].fillna(col_stats)
      elif is_string_dtype(df[column]):
        col_mode = df[column].value_counts().index[0] # mode
        df[column] = df[column].fillna(col_mode)
    return df
  else:
    for column in columns:
      if is_numeric_dtype(dataframe[column]):
        col_stats = fill_method(dataframe[column]) # mean, median, mode...
        dataframe[column] = dataframe[column].fillna(col_stats)
      elif is_string_dtype(dataframe[column]):
        col_mode = dataframe[column].value_counts().index[0] # mode
        dataframe[column] = dataframe[column].fillna(col_mode)