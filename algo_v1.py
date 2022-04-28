import pandas as pd

#read df from csv
dfnorm = pd.read_csv (r'sample_data4.csv',sep=";")
print (dfnorm)

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
frames = [dfeil, dfnorm]

#merge dfs sorting x = dfeil, y = df
dfmerge = pd.concat(frames, keys=["Eil","Normal"])
print(dfmerge)

#export dfmerge to xlsx
#dfmerge.to_excel('output.xlsx', sheet_name='Sheet1')
from tkinter import *
root = Tk()
root.title("Pakete")
root.geometry("500x500")
listbox_frame=Frame(root,borderwidth=5, relief=SUNKEN)
listbox_frame.pack(pady=120)
 
listbox=Listbox(listbox_frame, height=120)
listbox.pack()

listbox.insert(END,"Pakete")
 
for item in [dfmerge["ID"]]:
    listbox.insert(END, item)
 
def list_item_selected():
    selection=listbox.curselection()
    if selection:
        print(listbox.get(selection[0]))
 
list_box_button = Button(listbox_frame,text='Paket auswählen', command=list_item_selected)
list_box_button.pack()

root.mainloop()

dfmerge.loc[(dfmerge['Month'] == list_item_selected), ['Amount']].sum()