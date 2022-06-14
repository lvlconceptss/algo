import math as m

m1 = float(input("m1:"))
m2 = float(input("m2:"))
r = float(input("r:"))

t = m.pow(r,2)
print(f"F= {9.81*m1*m2/t} N")