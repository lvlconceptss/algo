value = input("Bitte geben Sie einen Wert für value ein: ")
t = input("Bitte geben Sie einen Datentyp für t ein (int,float,bool,string): ")

if t == "string":
    str(value)
    print("value kann String sein")
elif t == "int":
    int(value)
    print("value kann Integer sein")
elif t == "float":
    float(value)
    print("value kann Float sein")
elif t == "bool":
    bool(value)
    print("value kann Boolean sein")
else:
    print("Fehler")