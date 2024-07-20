def main():
    # TODO: Demandez la taille de l'utilisateur en centimètres et stockez le résultat dans une variable : height
    height = float(input("Veuillez entrer votre taille en centimètres : "))

    # TODO : afficher "Désolé, vous êtes trop petit pour ce manège. Essayez un autre carrousel."
    # si la taille est inférieure à 100 (exclus)
    if height < 100:
        print("Désolé, vous êtes trop petit pour ce manège. Essayez un autre carrousel.")

    # TODO : afficher "Profitez de votre tour !" si la taille est supérieure ou égale à 100 et inférieure ou égale à 150
    elif 100 <= height <= 150:
        print("Profitez de votre tour !")

    # TODO : afficher "Désolé, vous êtes trop grand pour celui-ci !" si la taille est supérieure à 150 (exclus)
    elif height > 150:
        print("Désolé, vous êtes trop grand pour celui-ci !")

if __name__ == '__main__':
    main()