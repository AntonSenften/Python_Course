# scope = är regionen som en variable kan kännas igen.


name = "Anton"              # "global scope" vilket betyder att den kan hämtas på inuti en funktion och utanför

def mitt_namn():
    name = "Senften"         # "local scope" känns bara igen inuti denhär funktionen
    print(name)

print(name)
mitt_namn()


# Python följer denna ordning L = local
#                             E = Enclosing
#                             G = global
#                             B = Built-in