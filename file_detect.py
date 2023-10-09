import os

#path = "C:\\Users\\Snef\\Desktop\\BroCode.txt"
path = "C:\\Users\\Snef\\Desktop\\BroCodeMap"

if os.path.exists(path):
    print("Platsen finns")
    if os.path.isfile(path):
        print("Det är en Fil")
    elif os.path.isdir(path):
        print("Det är en map")
else:
    print("Platsen finns inte")