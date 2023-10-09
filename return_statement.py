# return statement = Med ett return statment kan du få tillbaks ett värde/objekt som du efterfrågar. 

def multiplikation(nr1, nr2):
    result = nr1 * nr2         # Man kan skippa dena line och bara skriva 'return nr1 * nr2' för att få mindre kod
    return result

# print(multiplikation(2,10))

x = multiplikation(2,10)
print(x)