# exception = handlingar som upptäcks under utförande av ett program som avbryter
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator/denominator
except ZeroDivisionError:
    print("De går inte att dela med 0, nötskal")
except ValueError:
    print("Endast siffror!")
else:
    print(result)


