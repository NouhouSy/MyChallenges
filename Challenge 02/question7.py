#7.	Obtenez le rayon d'un cercle en utilisant une invite. Calculez l'aire (area = pi x r x r) 
# et la circonférence (c = 2 x pi x r) où pi = 3.14.
rayon = float(input("Veuillez entrez le rayon du cercle : "))
pi = 3.14
aire_cercle = pi * rayon * rayon
circonference = 2 * pi * rayon
print(f"L'aire du cercle est : {aire_cercle}")
print(f"La circonférence du cercle est : {circonference}")