import shutil  

# copyfile() = kopierar innehållet i en fil
# copy() = copyfile() + tillåtelse + destinationen kan vara en map
# copy2() = copy() + kopierar också metadata, vilket är när filen skapades eller ändrades

shutil.copyfile("C:\\Users\\Snef\\Desktop\\BroCode.txt","C:\\Users\\Snef\\Desktop\\BroCode3.txt")    # 2 argument (src,dst) source,destination