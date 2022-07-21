from sklearn import preprocessing

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