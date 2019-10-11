import pandas as pd
import numpy as np

from sqlalchemy import create_engine


"""
Reading and creating csv or xlsx file
"""
csv_file = pd.read_csv('..\FolderFile\example.csv', index_col=0)

csv_file.to_csv('..\FolderFile\my_output',index=False)
pd.read_csv('..\FolderFile\my_output')

"""
Read HTML 
"""

# data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# data[0].head()
#
# data[0].to_csv('..\FolderFile\Banks.csv', index=False)


"""
Creates SQL engine in memory
"""

engine = create_engine('sqlite:///:memory:')
csv_file.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)