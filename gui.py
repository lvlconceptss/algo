def gui():
    from tkinter import *
    root = Tk()

    listbox_frame=Frame(root,borderwidth=5, relief=SUNKEN)
    listbox_frame.pack(pady=120)
 
    listbox=Listbox(listbox_frame, height=120)
    listbox.pack()

    listbox.insert(END,"Pakete")
 
    for item in [dfmerge["Gewicht"]]:
    listbox.insert(END, item)
 
    def list_item_selected():
        selection=listbox.curselection()
        if selection:
            print(listbox.get(selection[0]))
 
    list_box_button = Button(listbox_frame,text='Paket auswählen', command=list_item_selected)
    list_box_button.pack()

    root.mainloop()

    dfmerge.loc[(dfmerge['Month'] == list_item_selected), ['Amount']].sum()