" python assignment for splitting a large csv files into smaller chunk of files"
" input type is csv"




import pandas as pd
import math
import os


df = pd.read_csv('input.csv')                 
file_size = os.stat('input.csv').st_size
split_size = 1000000
files = file_size/split_size
chunks=df.shape[0]//files
for i,chunk in enumerate(pd.read_csv(filepath, chunksize=chunks)):
    chunk.to_csv('C:\\Users\\anshetty\\OneDrive - Informatica\\Documents\\12\\input_{}.csv'.format(i), index=False)
