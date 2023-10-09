import os

source = "C:\\Users\\Snef\\Desktop\\BroCodeMove.txt"
destination = "C:\\Users\\Snef\\Documents\\BroCodeMove.txt"

try:
    if os.path.exists(destination):
        print("Det finns redan en fil med samma namn")
    else:
        os.replace(source,destination)
        print(source+" flyttades")
except FileNotFoundError:
    print(source+" kunde inte hittas")