#5.	Écrivez un script qui demande à l'utilisateur d'entrer les côtés a, b et c du triangle. 
#Calculez le périmètre du triangle (perimeter = a + b + c).
cote_a = float(input("Veuillez entrez la valeur du côté a : "))
cote_b = float(input("Veuillez entrez la valeur du côté b : "))
cote_c = float(input("Veuillez entrez la valeur du côté c : "))
perimetre = cote_a + cote_b + cote_c
print(f"Le périmètre du triangle est : {perimetre}")