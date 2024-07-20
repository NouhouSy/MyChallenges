#11.	Calculez la valeur de y (y = x^2 + 6x + 9). Essayez d'utiliser différentes valeurs de x 
#et trouvez à quelle valeur de x y sera égal à 0.
# Définir l'équation y = x^2 + 6x + 9
def equation(x):
    return x**2 + 6*x + 9
valeurs_de_x = [-4, -3, 0, 2]
for x in valeurs_de_x:
    y = equation(x)
    print(f"Pour x = {x}, y = {y}")