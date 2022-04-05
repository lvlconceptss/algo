import pandas as pd

df = pd.read_csv (r'sample_data4.csv',sep=";")
print (df)

#df = df.sort_values(['Gewicht'],
#              ascending = [True])

#df = df.sort_values(['Einlieferung', 'Gewicht'],
#              ascending = [True, True])


df.sort_values(by=['Einlieferung','Gewicht'], inplace=True,
               ascending = [True, True])

print(df)