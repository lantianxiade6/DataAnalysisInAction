import pandas as pd
from pandas import Series, DataFrame

score =DataFrame(pd.read_excel('./05/data.xlsx'))
score.to_excel('./05/data1.xlsx')

print(score)