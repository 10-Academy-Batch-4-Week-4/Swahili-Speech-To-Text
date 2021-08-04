import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../')))



class DfHelper:

  def __init__(self):
    pass

  def to_csv(self, csv_path, index=False):
    try:
      df =pd.to_csv(csv_path, index=index)


    except Exception:
        pass

  def read_csv(self, csv_path, missing_values=[]):
    try:
     
      df = pd.read_csv(csv_path, parse_dates = True,low_memory = False, index_col = 'Date', na_values=missing_values)

      return df
    except FileNotFoundError:
        pass
  
  


