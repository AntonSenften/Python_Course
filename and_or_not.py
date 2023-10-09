temp = int(input("Hur många grader är det ute?: "))

if temp >= 15 and temp <= 30:
    print("Skönt!")
    print("Bra temperatur för att vara utomhus.")
elif temp < 15 and temp >= 0:
    print("Brr, lite kyligt!")
    print("Glöm inte jackan!")
elif temp < 0:
    print("Minus grader!?")
    print("Jag hade nog stannat inne!")
elif temp >30 and temp <= 35:
    print("Oj, väldigt varmt idag!")
    print("Glöm inte solkräm")
elif temp >35:
    print("Lite för varmt kanske.")
    print("Bäst att hålla sig inomhus med AC:n på!")
else:
    print("error")
    