# *args = en parameter till en funktion, används för att man ska kunna acceptera ett varierat antal argument i en funktion

def add(*args):
    sum = 0           # start summan
    for i in args:    # i = index, alltså platsen innuti arguementet. 
        sum += i
    return sum

print(add(1,4,3,2,7))