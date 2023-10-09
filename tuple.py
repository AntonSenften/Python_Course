# tuple = en kollektion information som är i ordning och oföränringsbar. Används för att gruppera data som är relaterad

student = ("Anton",21,"Man")

print(student.count("Anton"))       # hur måga gånger ett värde finns i en defintion
print(student.index("Man"))         # vart ett specifikt värde ligger någonstans i defenitionen 0 för först 1 för nästa osv..

for x  in student:                  # ett sett att se vilka värden som finns i en defenition
    print(x)

if "Anton" in student:              # Letar efter ett specifikt värde 
    print("Anton är här!")