# Genom att använda [] runt en variabel kan man skapa en rad av olika ting som variabel skall vara definerade som istället för bara en grej.

food = ["pizza","Hamburgare","Hotdog","Spaghetti"]

food[0] = "shusi"
# print(food[0])

#food.append("Glass")          # Lägger till glass sist på listan
#food.remove("Spaghetti")      # tar bort vald grej, i detta fall spaghetti
#food.pop()                    # Tar bort de sista på listan
#food.insert(0,"Tårta")        # Lägger till ett grej på vald plats, i detta fallet 0 som är först
#food.sort()                   # Sorterar listan i alfabets ordning
#food.clear()                  # rensar listan

for x in food:
    print(x)