import pandas as pd
technologies = ({
    'Courses':["Spark","Hadoop","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,20000],
    'Duration':['30days','35days','40days','50days','60days'],
    'Discount':[1000,2300,1500,1200,2500]
               })
df = pd.DataFrame(technologies, index = ['r1','r2','r3','r4','r0'])
print(df)
