#3. Déclarez une variable nommée company et assignez-lui la valeur initiale "Coding For All".
compagny = "Coding For All"

#4. Imprimez la variable company en utilisant _print()_.
print("4-",compagny)

#5. Imprimez la longueur de la chaîne company en utilisant la méthode _len()_ et _print()_.
print("5- La longeur de cette chaine est : ", len(compagny))

#6. Changez tous les caractères en majuscules en utilisant la méthode _upper()_.
print(f"6- La conversion de la chaine : '{compagny}' en majuscule est : '{compagny.upper()}' ")

#7. Changez tous les caractères en minuscules en utilisant la méthode _lower()_.
print(f"7- La conversion de la chaine : '{compagny}' en miniscule est : '{compagny.lower()}'")

#8. Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne _Coding For All_.
print(f"8- {compagny} \n - En capitalize : {compagny.capitalize()} \n - En title : {compagny.title()}  \n - En swapcase : {compagny.swapcase()}")

#9. Coupez (slice) le premier mot de la chaîne _Coding For All_.
chaine = compagny[6:]
print(f"9- La nouvelle chaine avec la coupure du premier mot est : {chaine}")

#10. Vérifiez si la chaîne _Coding For All_ contient le mot Coding en utilisant les méthodes 
#index, find ou autres méthodes.
if "Coding" in compagny:
    print(f"10.1- Le mot 'Coding' existe dans la chaîne à l'indice n° : {compagny.find('Coding')}")
else:
    print(f"Ce mot n'existe pas dans {compagny}")
if "Coding" in compagny:
    print(f"10.2- Le mot 'Coding' existe dans la chaîne à l'indice n° : {compagny.index('Coding')}")
else:
    print(f"Ce mot n'existe pas dans {compagny}")
    
#11. Remplacez le mot coding dans la chaîne 'Coding For All' par Python.
compagny = "Python for All"
print(f"11- La nouvelle chaîne est : {compagny}")

#12. Changez  Python for All en Python for Everyone en utilisant la méthode replace ou d'autres méthodes.
print(f"12- Le remplacement de la chaîne : '{compagny}' est : {compagny.replace("Python for All", "Python for Everyone")}")

#13. Divisez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()).
compagny = "Coding For All"
print(f"13- La division de la chaîne de caractère : {compagny} est : {compagny.split(sep=" ")}")

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divisez la chaîne au niveau de la virgule.
chaines = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"14- La division de la chaîne au niveau de la virgule est : {chaines.split(sep=",")}")

#15. Quel est le caractère à l'index 0 dans la chaîne _Coding For All_.
print(f"15- Le caractère au niveau de l'index 0 de '{compagny}' est : {compagny[0]}")

#16. Quel est le dernier index de la chaîne _Coding For All_.
print(f"16- Le dernier index de la chaîne '{compagny}' est : {compagny[13]}")

#17. Quel caractère se trouve à l'index 10 dans la chaîne "Coding For All".
print(f"17- Le caractère qui se trouve à  l'index n°10 de la chaîne '{compagny}' est : {compagny[10]}")

#18. Créez un acronyme ou une abréviation pour le nom 'Python For Everyone'.
var1  = "Python For Everyone"
print(f"18- L'accronyme de '{var1}' est : {var1.replace('Python For Everyone', 'PFE')}")

#19. Créez un acronyme ou une abréviation pour le nom 'Coding For All'.
var2 = "Coding For All"
print(f"19- L'accronyme de '{var2}' est : {var2.replace('Coding For All', 'CFA')}")

#20. Utilisez l'index pour déterminer la position de la première occurrence de C dans Coding For All.
chaine = "Coding For All"
position_c = chaine.index('C')
print(f"20- La posisition de la première occurence de 'C' est : {position_c}")

#21. Utilisez l'index pour déterminer la position de la première occurrence de F dans Coding For All.
chaine = "Coding For All"
position_f = chaine.index('F')
print(f"21- La posisition de la première occurence de 'F' est : {position_f}")

#22. Utilisez rfind pour déterminer la position de la dernière occurrence de l dans Coding For All People.
chaine = "Coding For All"
position_l = chaine.rindex('l')
print(f"22- La dernière occurence de 'l' est : {position_l}")

#23. Utilisez index ou find pour trouver la position de la première occurrence du mot 'because' dans la phrase suivante : 
#'You cannot end a sentence with because because because is a conjunction'.

texte = "You cannot end a sentence with because because because is a conjunction"
position_1_because = texte.find("because")
print(f"23- La position de la première occurence du mot 'because' est : {position_1_because}")

#24. Utilisez rindex pour trouver la position de la dernière occurrence du mot because dans la phrase suivante : 
# 'You cannot end a sentence with because because because is a conjunction'.
position_dernier_because = texte.rfind("because")
print(f"24- La position de la dernière occurence du mot 'because' est : {position_dernier_because}")

#25. Coupez la phrase 'because because because' dans la phrase suivante : 
#'You cannot end a sentence with because because because is a conjunction'.
texte = "You cannot end a sentence with because because because is a conjunction"
nouvelle_phrase = texte.replace("because because because", "")
print(f"25- La nouvelle chaine sans 'because' est : {nouvelle_phrase}")

#28. La chaîne '\'Coding For All' commence-t-elle par une sous-chaîne _Coding_ ?
chaine = "\'Coding For All"
commence_par_Coding = chaine.startswith("Coding")
print(f"28- La chaîne commence t-elle par 'Coding' : {commence_par_Coding}")

#29. La chaîne 'Coding For All' se termine-t-elle par une sous-chaîne _coding_ ?
var = "Coding For All"
termine_par_coding = var.endswith("coding")
print(f"29- La chaine 'Coding For All' se termine t-elle par 'coding' : {termine_par_coding}")

#30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, 
#supprimez les espaces à gauche et à droite dans la chaîne donnée.
chaine = "&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;"
chaine_propre = chaine.replace("&nbsp;", " ")
chaine_propre = chaine_propre.strip()
print(f"30- La nouvelle chaine sans les espaces est :  {chaine_propre}")

#31.La liste suivante contient les noms de certaines bibliothèques python : 
#['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Joignez la liste avec une chaîne de caractères hash avec espace.
librairies = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joindre_librairies = " ".join(librairies)
print(f"31- La nouvelle chaine sans les caractères est : {joindre_librairies}")

#32.Utilisez la séquence d'échappement de nouvelle ligne pour séparer les phrases suivantes.
#I am enjoying this challenge.
#I just wonder what is next.
phrase1 = "I am enjoying this challenge"
phrase2 = "I just wonder what is next"
print(f"32- {phrase1} \n    {phrase2}")

#33.Utilisez la séquence d'échappement de tabulation pour écrire les lignes suivantes.
#	Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("33.1- Name" + "\t" + "Age" + "\t" + "Country" + "\t" + "City")
print("33.2- Asabeneh " + "\t" + "250" + "\t" + "Finland" + "\t" + "Helsinki")

#35.Utilisez la méthode de formatage de chaîne pour afficher ce qui suit :
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
output = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print("35-",output)

#36.Réalisez ce qui suit en utilisant les méthodes de formatage de chaîne :
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 
# Définir les variables
a = 8
b = 6

addition = f"{a} + {b} = {a + b}"
soustraction = f"{a} - {b} = {a - b}"
multiplication = f"{a} * {b} = {a * b}"
division = f"{a} / {b} = {a / b:.2f}"
modulo = f"{a} % {b} = {a % b}"
division_entiere = f"{a} // {b} = {a // b}"
puissance = f"{a} ** {b} = {a ** b}"


print("36.1- ",addition)
print("36.2- ",soustraction)
print("36.3- ",multiplication)
print("36.4- ",division)
print("36.5- ",modulo)
print("36.6- ",division_entiere)
print("36.7- ",puissance)