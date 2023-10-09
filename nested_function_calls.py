# nested function calls = kallar på en funtkion inom en annan funktion, den "innersta löses först, etc". värdet från innersta används för att lösa nästa.

# num = input("Ange ett positivt heltal: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)                   # Istället för alla dessa rader kan då en nested function kallas på en rad i ordningen uppifrån och ned.

print(round(abs(float(input("Ange ett positivt heltal: ")))))
