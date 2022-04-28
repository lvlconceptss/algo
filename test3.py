from tkinter import *
import pandas as pd 

#read df from csv
dfnorm = pd.read_csv (r'sample_data4.csv',sep=";")
print (dfnorm)



master = Tk()

master.title("Paketeverwaltung")
master.geometry("500x500")

var1 = IntVar()
Checkbutton(master, text=dfnorm.iloc[[1]], variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text=dfnorm.iloc[[2]], variable=var2).grid(row=1, sticky=W)
mainloop()