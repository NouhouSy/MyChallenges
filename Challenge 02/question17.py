#17. Les nombres pairs sont divisibles par 2 et le reste est zéro. 
#Comment vérifiez-vous si un nombre est pair ou non en utilisant python ?
nombre = int(input("Entrez un nombre svp : "))
if nombre % 2 == 0:
    print(f"{nombre} est un nombre pair")
else:
    print(f"{nombre} n'est pas un nombre pair")