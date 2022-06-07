
import pandas as pd

def init():
    pd.DataFrame(columns=["Einlieferung","Gewicht","Status","ID"]).to_csv('resttag.csv', sep=";", index=False)

#only use if repository is not initialized
#init()

#import df from csv
dfnorm = pd.read_csv (r'sample_data4.csv',sep=";")
#import rest of df from csv
dfrest = pd.read_csv (r'resttag.csv',sep=";")

def bearbeitung(dfold):
    dfold.to_excel('Paketliste.xlsx', sheet_name='Pakete')
    print("Pakete die heute für den Versand vorgesehen sind:  ", dfold.shape[0])
    i = int(input("Bis zu welchem Paket wurde bearbeitet? "))
    print(dfold)
    dfold.drop(dfold.index[0:i], axis=0, inplace=True)
    print(dfold)
    dfold.to_csv('resttag.csv', sep=";", index=False)

##Beginn Algorithmus
#split eillieferung to differrent df
dfeil = dfnorm[dfnorm['Status'] == 1]
#remove rows with status 1 from df
dfnorm = dfnorm[dfnorm['Status'] != 1]

#sort dfeil by Gewicht 
dfeil = dfeil.sort_values(['Gewicht'],ascending = [True])
print("Eil: ")
print (dfeil)

#sort dfnormal by Gewicht
dfnorm = dfnorm.sort_values(by=['Gewicht'], ascending = [True])
print("Normal:")
print(dfnorm)

#define merge list
frames = [dfrest, dfeil, dfnorm]

#merge dfs sorting x = dfeil, y = df
dfmerge = pd.concat(frames, keys=["Rest","Eil","Normal"])
print(dfmerge)
##Ende Algorithmus


#Start der Bearbeitung durch Mitarbeiter
bearbeitung(dfmerge)

