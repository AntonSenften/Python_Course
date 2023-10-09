try:
    with open("C:\\Users\\Snef\\Desktop\\BroCode.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Kunde inte hitta file")
    


