age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble, lequel est plus grand ?
age_set = set(age)
length_list = len(age)
length_set = len(age_set)

print("1- Longueur de la liste est : ", length_list)
print("1- Longueur de l'ensemble est : ", length_set)

if length_list > length_set:
    print("- La liste est plus grande.")
elif length_list < length_set:
    print("- L'ensemble est plus grand.")
else:
    print("Les deux ont la même longueur.")
    
#2. Expliquez la différence entre les types de données suivants : string, list, tuple et set.
# String (chaîne de caractères) :
# Type de données immuable (non modifiable).
# Utilisée pour stocker du texte.
# Déclarée en utilisant des guillemets simples (' ') ou doubles (" ").
# Exemple : "hello".

# List (liste) :
# Type de données mutable (modifiable).
# Utilisée pour stocker une collection ordonnée d'éléments.
# Déclarée en utilisant des crochets ([ ]).
# Les éléments peuvent être de types différents.
# Exemple : [1, 2, 'three', 4.0].

# Tuple :
# Type de données immuable (non modifiable).
# Utilisée pour stocker une collection ordonnée d'éléments.
# Déclarée en utilisant des parenthèses (( )).
# Les éléments peuvent être de types différents.
# Exemple : (1, 2, 'three', 4.0).

# Set (ensemble) :
# Type de données mutable (modifiable), mais les éléments doivent être immuables.
# Utilisée pour stocker une collection non ordonnée d'éléments uniques.
# Déclarée en utilisant des accolades ({ }).
# Exemple : {1, 2, 3, 4}.

#3. _I am a teacher and I love to inspire and teach people._ Combien de mots uniques ont été utilisés dans la phrase ? 
# Utilisez les méthodes split et set pour obtenir les mots uniques.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
print("3- Nombre de mots uniques:", num_unique_words)
print("3- Mots uniques:", unique_words)
