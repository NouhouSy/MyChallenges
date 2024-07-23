db_path = "./database.txt"

def create_multi(contacts):
    data = "\n".join(contacts) + "\n"
    with open(db_path, "w") as db:
        success = db.write("\n" + data)
    return success

def create(args):
    new_contact = f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n"
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
        for contact in contacts:
            if args['phone'] in contact:
                print("Numéro de téléphone déjà existant.")
                return False
    with open(db_path, "a") as db:
        db.write(new_contact)
    return True

def search(phone):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
    results = [contact for contact in contacts if contact.endswith(phone)]
    return results

def search_all():
    with open(db_path, "r") as db:
        contacts = db.read().strip().split("\n")
    return contacts

def delete(contact):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
        contacts = [c for c in contacts if c.strip() != contact.strip()]
    return create_multi(contacts)

def save_controller(args):
    return create(args)

def search_controller(phone):
    results = search(phone)
    if not results:
        print("Contact non trouvé.")
        return []
    contact_vals = [result.split(',') for result in results]
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
    return contacts

def delete_controller(contact):
    contact = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return delete(contact)

def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"Nom: {lastname}\nPrénom: {firstname}\nAdresse: {address}\nTéléphone: {phone}\n"
    print(contact_string)

def afficher_annuaire():
    print("\nAnnuaire Téléphonique :\n")
    contacts = search_all()
    for contact in contacts:
        if contact.strip():
            afficher_contact(*contact.split(','))

def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": "", "firstname": "", "address": "", "phone": ""}
    lastname = input("Nom: ").strip() or contact["lastname"]
    firstname = input("Prénom: ").strip() or contact["firstname"]
    address = input("Adresse: ").strip() or contact["address"]
    phone = input("Téléphone: ").strip() or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}
    
    def click_save(args):
        success = save_controller(args)
        if success:
            print("Contact ajouté avec succès.")
        else:
            print("Échec de l'ajout du contact.")
    if save:
        click_save(args)
    else:
        afficher_contact(lastname, firstname, address, phone)

def click_search(phone):
    return search_controller(phone)

def rechercher_contact():
    phone = input("Entrez le numéro de téléphone complet à rechercher: ").strip()
    contacts = click_search(phone)
    if contacts:
        afficher_contact(*contacts[0].values())
        print("Voulez-vous..")
        print("3. Modifier ce contact")
        print("4. Supprimer ce contact")
        print("5. Retourner au menu principal")
        sub_action = int(input(" >> "))
        if sub_action == 5:
            pass
        elif sub_action == 4:
            supprimer_contact()
        elif sub_action == 3:
            supprimer_contact(modify=True)
    else:
        print("Contact non trouvé.")

def supprimer_contact(modify=False):
    phone = input("Entrez le numéro de téléphone complet du contact:").strip()
    contacts = click_search(phone)
    if contacts:
        afficher_contact(*contacts[0].values())
        success = delete_controller(contact=contacts[0])
        if success and not modify:
            print("Le contact a été supprimé avec succès.")
        elif success and modify:
            ajouter_contact(contact=contacts[0], save=True)
    else:
        print("Contact non trouvé.")

if __name__ == "__main__":
    afficher_annuaire()
    while True:
        print("Entrez votre action parmi les suivantes:")
        print("1. Rechercher un contact")
        print("2. Ajouter un contact")
        print("0. Sortir de l'application")
        action = int(input(" >> "))
        if action == 1:
            rechercher_contact()
        elif action == 2:
            ajouter_contact(save=True)
        elif action == 0:
            break
        else:
            print("Opération non supportée pour le moment.")