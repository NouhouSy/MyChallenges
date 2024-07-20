#10.	Comparez les pentes des tâches 8 et 9.
# Pente de l'équation y = 2x - 2
pente1 = 2
x1, y1 = 2, 2
x2, y2 = 6, 10
pente2 = (y2 - y1) / (x2 - x1)
print(f"La pente de l'équation y = 2x - 2 est : {pente1}")
print(f"La pente entre les points (2, 2) et (6, 10) est : {pente2}")
if pente1 == pente2:
    print("Les pentes sont égales.")
else:
    print("Les pentes sont différentes.")
