#18. Vérifiez si la division entière de 7 par 3 est égale à la valeur convertie en entier de 2.7.
x = 7
y = 3
division_entiere = 7 // 3
k = 2.7
conversion = int(k)
print(f"La division entière de 7 par 3 est : {division_entiere}")
print(f"La conversion de '2.7' en entier est : {conversion}")
if division_entiere == conversion:
    print(f"La division entière de 7 par 3 est égal à la conversion de 2.7 en entier : {division_entiere} = {conversion}")
else:
    print("Ce n'est pas égal")