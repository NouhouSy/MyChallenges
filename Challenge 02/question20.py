#20. Vérifiez si int('9.8') est égal à 10.
nb1 = '9.8'
nb2 = 10
conversion1 = float(nb1)
conversion2 = int(conversion1)
print("nombre 1 est égal à : ", nb1)
print("nombre 2 est égal à ", nb2)
if conversion2 == nb2:
    print(f"{conversion2} = {nb2}")
else:
    print(f"La conversion de '9.8' en entier est égal à : {conversion2} qui n'est pas égal à : {nb2}")