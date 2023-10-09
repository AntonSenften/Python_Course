# dictionary = en förändringsbar kollektion som inte är i ordning av unika nyckel värde-par. Används för att komma åt ett värde snabbt - key:value

huvudstäder = {'USA':'Washington DC',
               "Indien" : "New Delih",
               "Kina" : "Peking",
               "Sverige" : "Stockholm"}

huvudstäder.update({'Tyskland':'Berlin'})
huvudstäder.pop('Kina')                 # Tar bort en nyckel och associreat värde till de i din lista.

# print(huvudstäder["Sverige"])         # Hämtar värdet asocierat med "Sverige" 
# print(huvudstäder.get("Tyskland"))    # Kollar om tyskland finns i defenitionen, ger inga fel meddelanden
# print(huvudstäder.values())           # Kollar vilka värden som finns
# print(huvudstäder.items())            # Kollar vilka nycklar som finns och vilket värde de år kopplade till
# print(huvudstäder.keys())             # Kollar vilka nycklar som finns

for key,value in huvudstäder.items():
    print(key,value)