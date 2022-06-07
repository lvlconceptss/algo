value = input("Geben Sie ihre Variable ein: ")
t=input("Auf welchen Datentyp soll geprüft werden(Moeglichkeiten: bool, string, int und float): ")

if (value.isalpha() or ''in value):
    if (value=='true'):
        if(t=='bool'):
            print(f'{value} ist ein bool')
        else:
            print(f'{value} ist kein {t}')
    elif (value=='false'):
        if(t=='bool'):
            print(f'{value} ist ein bool')
        else:
            print(f'{value} ist kein {t}')

    else:
        if(t=='string'):
            print(f'{value} ist ein String')
        else:
            print(f'{value} ist kein {t}')

elif (value.isdecimal()):
    if(t=='int'):
        print(f'{value} ist ein Int')
    else:
        print(f'{value} ist kein {t}')

elif "." in value:
    if(t=='float'):
        print(f'{value} ist ein float')
    else:
        print(f'{value} ist kein {t}')



else:
    print('error')