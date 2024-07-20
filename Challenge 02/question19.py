#19. Vérifiez si le type de '10' est égal au type de 10.
type1 = '10'
type2 = 10
print("Le type de '10' est : ", type(type1))
print("Le type de 10 est : ", type(type2))
if type(type1) == type(type2):
    print("Ils sont égal")
else:
    print("Ils ne sont pas égal")