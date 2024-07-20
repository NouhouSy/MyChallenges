#6.	Obtenez la longueur et la largeur d'un rectangle en utilisant une invite. 
#Calculez son aire (area = length x width) et son périmètre (perimeter = 2 x (length + width)).
longueur = float(input("Veuillez entrez la longueur du rectangle : "))
largeur = float(input("Veuillez entrez la largeur du rectangle : "))
aire = longueur * largeur
perimetre = 2 * (longueur + largeur)
print(f"L'aire du rectangle est : {aire}")
print(f"Le périmètre du rectangle est : {perimetre}")