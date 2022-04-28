import pandas as pd

#read df from csv
dfnorm = pd.read_csv (r'sample_data4.csv',sep=";")
print (dfnorm)

#split eillieferung to differrent df
dfeil = dfnorm[dfnorm['Status'] == 1]
#remove rows with status 1 from df
dfnorm = dfnorm[dfnorm['Status'] != 1]
#sort dfeil by Einlieferung
dfeil = dfeil.sort_values(['Gewicht'])
print("Eillieferung:")
print (dfeil)

#sort df by Einlieferung and Gewicht
dfnorm = dfnorm.sort_values(by=['Gewicht'], kind='stable', 
               ascending = [True])
print("Normal:")
print(dfnorm)

#define merge list
frames = [dfeil, dfnorm]

#merge dfs sorting x = dfeil, y = df
dfmerge = pd.concat(frames, keys=["x","y"])
print(dfmerge)

#export dfmerge to xlsx
dfmerge.to_excel('output.xlsx', sheet_name='Sheet1')