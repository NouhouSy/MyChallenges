it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Trouvez la longueur de l'ensemble it_companies.
longueur_it_companies = len(it_companies)
print("1- La longueur de 'it_companies' est : ", longueur_it_companies)

#2. Ajoutez 'Twitter' à it_companies.
it_companies.add('Twitter')
print("2- La nouvelle liste après l'ajout de 'Twitter' est : ", it_companies)

#3. Insérez plusieurs entreprises IT à la fois dans l'ensemble it_companies.
new_companies = {'Netflix', 'Spotify', 'Adobe'}
it_companies.update(new_companies)
print("3- La nouvelle liste après l'ajout de plusieurs entreprises:", it_companies)

#4. Supprimez l'une des entreprises de l'ensemble it_companies.
it_companies.remove('IBM') 
print("4- La nouvelle liste après la suppression de 'IBM':", it_companies)

#5. Quelle est la différence entre `remove` et `discard` ?
try:
    it_companies.remove('Amazon')
    print("5- La nouvelle liste après la suppression de 'Amazon' avec remove est : ", it_companies)
except KeyError:
    print(" 'Amazon' n'existe pas dans l'ensemble.")

it_companies.discard('Oracle')
print("5- La nouvelle liste après la suppression de 'Oracle' avec discard est : ", it_companies)
