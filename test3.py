import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


import tkinter as tk
from turtle import left
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

list = dfmerge.values.tolist()



root = tk.Tk()
root.title('Paketeverwaltung')
root.geometry('620x200')

# define columns
columns = ('Einlieferung', 'Gewicht', 'Status', 'ID')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('Einlieferung', text='Einlieferung')
tree.heading('Gewicht', text='Gewicht')
tree.heading('Status', text='Status')
tree.heading('ID', text='ID')


# add data to the treeview
for contact in list:
    tree.insert('', tk.END, values=contact)
    


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=1, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=2, sticky='ns')

#var1 = tk.IntVar()
#c1 = tk.Checkbutton(root,variable=var1).grid(row=1, column=3 ,padx='5',sticky='ew')
#c1.pack()
#c1.place(x=10,y=25)

# run the app
root.mainloop()