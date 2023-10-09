import random

val = ["sten", "sax", "påse"]
running = True

while running:
    dator = random.choice(val)
    spelare = None

    while spelare not in val:
       spelare = input("sten, sax eller påse?: ").lower()

    if spelare == dator:
        print("bot: ", dator)
        print("spelare: ", spelare)
        print("Ingen vinnare!")

    elif spelare == "sten":
        if dator == "påse":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du förlorade!")
        if dator == "sax":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du vann!")
    elif spelare == "sax":
        if dator == "påse":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du vann!")
        if dator == "sten":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du förlorade!")
    elif spelare == "påse":
        if dator == "sten":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du vann!")
        if dator == "sax":
            print("bot: ", dator)
            print("spelare: ", spelare)
            print("Du förlorade!")

    if not input("Spela igen? (ja/nej): ").lower() == "ja":
        running = False
print("Hej da!")
