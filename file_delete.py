import os
import shutil

path = "C:\\Users\\Snef\\Desktop\\BroCode3.txt"

try:
    #os.remove(path)         # delete file
    #os.rmdir(path)          # delete mapp
    #shutil.rmtree(path)     # delete mapp med filer
except FileNotFoundError:
    print("Kunde inte hitta filen")
except PermissionError:
    print("Du har inte tillåtelse ta bort")
except OSError:
    print("Du kan inte ta bort mappar med innehåll med denna fuktion")
else:
    print(path+" togs bort")