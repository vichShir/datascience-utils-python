import re
import pandas as pd
import numpy as np
import itertools
from collections import Counter

EMAIL_PATTERN = "([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
PHONE_PATTERN_1 = "(\(?\d{2}\)?\s)?(\(?\d{1,2}\)?\s)?(\d{4,6}[-. ]?\d{4,5})" # +55 (11) 123456-7890
PHONE_PATTERN_2 = "(\d{10,13})" #5511234567890
PHONE_PATTERN = PHONE_PATTERN_1 + "|" + PHONE_PATTERN_2
YEAR_PATTERN = "\s19\d{2}|20\d{2}"


def find_email(txt):
  return re.findall(EMAIL_PATTERN, txt)


def find_phone(txt):
  phone_list = []
  numbers_found = re.findall(PHONE_PATTERN, txt)
  for number in numbers_found:
    number = ''.join(number)
    phone = re.sub('[\s().+-]', '', number) # Remove special characters
    phone_list.append(phone)
  return phone_list


def find_year(txt):
  return list(map(str.strip, re.findall(YEAR_PATTERN, txt)))


def remove_multiple_spaces(txt):
  return re.sub(r'\W+', ' ', txt)


def match_elements_in_dataframe(src_df, src_col, elements_list):
    # perform first quick search (duplicates not included)
    df1 = src_df[src_df[src_col].isin(elements_list)]
    
    # list duplicated elements and count how many
    d = [(v, c-1) for v, c in Counter(elements_list).items() if c > 1]
    l = [([v]*c) for v, c in d] # create a list with duplicated elements
    
    # concat lists into one
    s = list(itertools.chain.from_iterable(l))

    # skip if there is no duplicated elements
    if len(s) > 0:
        df_final = df1.copy()
    else:
        # do final search with the duplicate ones
        df2 = [src_df[src_df[src_col].values == smi] for smi in s]
        df2 = pd.concat(df2, axis=0)

        # concat the initial search with the last search
        df_final = pd.concat([df1, df2], axis=0).reset_index(drop=True)
    
    # reorder
    df_list = pd.DataFrame({src_col: elements_list})
    df_list['g'] = df_list.groupby(src_col).cumcount()
    df_final['g'] = df_final.groupby(src_col).cumcount()
    df_final = df_list.merge(df_final).drop(columns=['g'])

    # remove source column
    df_final = df_final.drop(columns=[src_col])

    return df_final