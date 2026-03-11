from pathlib import Path


def afficher_message_accueil():
    print("Bienvenue au jeu de casino")


def demander_pseudo():
    pseudo = input("Je suis Python, quel est votre pseudo ?\n").strip()
    while not pseudo:
        print("Le pseudo ne peut pas être vide.")
        pseudo = input("Je suis Python, quel est votre pseudo ?\n").strip()
    return pseudo


def afficher_message_bienvenue(pseudo, dotation=10):
    print(f"Hello, {pseudo}, vous avez {dotation} €. Très bien ! Installez-vous SVP à la table de pari.")


def demander_voir_regles():
    choix = input("Voulez-vous afficher les règles du jeu ? Oui ou Non ?\n").strip().lower()
    while choix not in ["oui", "non"]:
        print("Réponse invalide. Entrez Oui ou Non.")
        choix = input("Voulez-vous afficher les règles du jeu ? Oui ou Non ?\n").strip().lower()
    return choix == "oui"


def afficher_regles():
    rules_path = Path(__file__).resolve().parent.parent / "domain" / "rule.txt"

    try:
        with open(rules_path, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("Le fichier des règles est introuvable.")


def demander_mise(minimum, maximum):
    while True:
        try:
            mise = int(input(f"Le jeu commence, entrez votre mise ({minimum} à {maximum} €) :\n"))
            if minimum <= mise <= maximum:
                print(f"Vous avez misé {mise} €. Très bien !")
                return mise
            print(f"Le montant saisi n'est pas valide. Entrez un montant entre {minimum} et {maximum} €.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def demander_nombre(minimum, maximum):
    while True:
        try:
            nb_user = int(input(f"Je viens de penser à un nombre entre {minimum} et {maximum}. Devinez lequel ?\n"))
            if minimum <= nb_user <= maximum:
                return nb_user
            print(f"Veuillez entrer un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def afficher_nombre_trop_grand():
    print("Votre nombre est trop grand.")


def afficher_nombre_trop_petit():
    print("Votre nombre est trop petit.")


def afficher_victoire(nb_coup):
    print(f"Bingo ! Vous avez gagné en {nb_coup} coup(s) !")


def afficher_defaite(nb_python):
    print(f"Perdu ! Le bon nombre était {nb_python}.")


def demander_continuer_jeu():
    reponse = input("Souhaitez-vous continuer la partie (O/N) ?\n").strip().lower()
    while reponse not in ["oui", "non", "o", "n"]:
        print("Réponse invalide. Entrez O/N ou Oui/Non.")
        reponse = input("Souhaitez-vous continuer la partie (O/N) ?\n").strip().lower()

    return reponse in ["oui", "o"]


def afficher_passage_niveau(level):
    print(f"Super ! Vous passez au Level {level}.")


def afficher_fin_partie(solde):
    print(f"Au revoir ! Vous finissez la partie avec {solde} €.")
