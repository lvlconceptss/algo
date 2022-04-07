import pandas as pd

df = pd.read_csv (r'sample_data4.csv',sep=";")
print (df)

# df = df.sort_values(['Einlieferung'],
#               ascending = [True])

# df = df.sort_values(['Einlieferung', 'Gewicht'],
#               ascending = [True, True])


#split eillieferung to differrent df
dfeil = df[df['Status'] == 1]
#remove rows with status 1 from df
df = df[df['Status'] != 1]
#sort dfeil by Einlieferung
dfeil = dfeil.sort_values(['Einlieferung'])
print("Eillieferung:")
print (dfeil)

#sort df by Einlieferung and Gewicht
df = df.sort_values(by=['Einlieferung', 'Gewicht'], kind='stable', 
               ascending = [True, True])
print("Normal:")
print(df)

#define merge list
frames = [dfeil, df]

#merge dfs sorting x = dfeil, y = df
dfmerge = pd.concat(frames, keys=["x","y"])
print(dfmerge)