
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
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

listmerge = dfmerge.values.tolist()



#GUI

#Main Window 

root = tk.Tk()
root.title("Paketverwaltung")
root.geometry("1024x700")
root.resizable(0,0)

#TreeView

class CbTreeview(ttk.Treeview):

    def __init__(self, master=None, **kw):
        kw.setdefault('style', 'cb.Treeview')
        kw.setdefault('show', 'headings')  # hide column #0
        ttk.Treeview.__init__(self, master, **kw)

        # create checheckbox images
        self._im_checked = tk.PhotoImage('checked',
                                         data=b'GIF89a\x0e\x00\x0e\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x02#\x04\x82\xa9v\xc8\xef\xdc\x83k\x9ap\xe5\xc4\x99S\x96l^\x83qZ\xd7\x8d$\xa8\xae\x99\x15Zl#\xd3\xa9"\x15\x00;',
                                         master=self)
        self._im_unchecked = tk.PhotoImage('unchecked',
                                           data=b'GIF89a\x0e\x00\x0e\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x02\x1e\x04\x82\xa9v\xc1\xdf"|i\xc2j\x19\xce\x06q\xed|\xd2\xe7\x89%yZ^J\x85\x8d\xb2\x00\x05\x00;',
                                           master=self)
        style = ttk.Style(self)
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders))

        # put image on the right
        style.layout('cb.Treeview.Row',
                     [('Treeitem.row', {'sticky': 'nswe'}),
                      ('Treeitem.image', {'side': 'right', 'sticky': 'e'})])

        # use tags to set the checkbox state
        self.tag_configure('checked', image='checked')
        self.tag_configure('unchecked', image='unchecked')

    def tag_add(self, item, tags):
        new_tags = tuple(self.item(item, 'tags')) + tuple(tags)
        self.item(item, tags=new_tags)

    def tag_remove(self, item, tag):
        tags = list(self.item(item, 'tags'))
        tags.remove(tag)
        self.item(item, tags=tags)

    def insert(self, parent, index, iid=None, **kw):
        item = ttk.Treeview.insert(self, parent, index, iid, **kw)
        self.tag_add(item, (item, 'unchecked'))
        self.tag_bind(item, '<ButtonRelease-1>',
        lambda event: self._on_click(event, item))

    def _on_click(self, event, item):
        """Handle click on items."""
        if self.identify_row(event.y) == item:
            if self.identify_column(event.x) == '#5': # click in 'Served' column
                # toggle checkbox image
                if self.tag_has('checked', item):
                    self.tag_remove(item, 'checked')
                    self.tag_add(item, ('unchecked',))
                else:
                    self.tag_remove(item, 'unchecked')
                    self.tag_add(item, ('checked',))



tree = CbTreeview(root, columns=("Einlieferung", "Gewicht", "Status", "ID", "Versand"),
                  height=400, selectmode="extended")

#Formatierung des Tree's
##Zeilen
tree.heading('Einlieferung', text='Einlieferung',anchor = 'nw')
tree.heading('Gewicht', text='Gewicht',anchor = 'nw')
tree.heading('Status', text='Status',anchor = 'nw')
tree.heading('ID', text='ID',anchor = 'nw')
tree.heading('Versand', text = 'Versand',anchor = 'nw')
##Spalten
tree.column('Einlieferung',stretch = 'false', anchor = 's' )
tree.column('Gewicht',stretch = 'false', anchor = 's' )
tree.column('Status',stretch = 'false', anchor = 's' )
tree.column('ID',stretch = 'false', anchor = 's' )

tree.pack(fill='both')

for contact in listmerge:
    tree.insert('', tk.END, values=contact)
    

#tree.grid(row=0, column=1, sticky='nsew')
tree.pack(side = 'left')

#Scrollbar 

#vsb = ttk.Scrollbar(root, orient="vertical")
#vsb.pack(side='right',fill='y')

#tree.configure(xscrollcommand = vsb.set)

root.mainloop()