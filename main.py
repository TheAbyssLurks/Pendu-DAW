import moteur_jeu
import affichage_pendu
import gestion_saisie
import dictionnaire


def affichage_menu():
    print("Jeu du pendu\n")
    print("\nRèglements")
    print("Vous devez trouver le mot rechercher avant que le dessin du bonhomme pendu soit completé.")
    print("- Vous avez 7 essais.")
    print("- Vous ne pouvez qu'utiliser des lettres.")
    print("- Vous avez droit à deux aides durant la partie :")
    print("     - Dévoiler une lettre automatiquement en écrivant 'devoiler'.")
    print("     - Dévoiler un indice sur le mot en écrivant 'indice'.\n")
    input("Appuyer sur une touche pour lancer une partie : ")


def jeu():
    # Création du mot pour la nouvelle partie.
    mot_rechercher = dictionnaire.tirage_mot(dictionnaire.liste_mot)
    # Création de la partie.
    mot_trouver = list("_" * len(mot_rechercher.mot))
    partie = moteur_jeu.Partie(0, -1, False, False, mot_rechercher.mot, mot_trouver, mot_rechercher.indice)

    # Affichage du pendu et des informations de la partie.
    affichage_pendu.affichage_pendu(partie.nb_erreurs)
    affichage_information(partie)

    while partie.etat == 0:
        saisie = gestion_saisie.gestion_saisie(partie)
        if saisie is True:
            partie.modification_mot_trouver()
        elif saisie is False:
            partie.gestion_erreurs()
        elif saisie == "indice":
            partie.modification_mot_trouver()
        elif saisie == "devoiler":
            partie.devoilement_lettre()
        elif saisie == "dejaentree":
            partie.modification_mot_trouver()

        partie.verification_mot()
        affichage_pendu.affichage_pendu(partie.nb_erreurs)
        affichage_information(partie)

    if partie.etat == 1:
        print("Vous avez gagné!")
    elif partie.etat == 2:
        print("Vous avez perdu.")


def affichage_information(partie):
    mot_rechercher = ""
    for lettre in partie.mot_trouver:
        mot_rechercher += lettre

    print("Mot recherché : ", mot_rechercher)
    print("Nombre d'erreurs :", partie.nb_erreurs + 1)
    print("Lettres utilisées", partie.lettre_utilisees)
    if partie.indice_utiliser == True:
        print("Indice : ", partie.indice)
    else:
        print("Indice : Non utilisé.")
    if partie.lettre_devoilee == True:
        print("Lettre dévoilée : ", partie.lettre_indice)
    else:
        print("Lettre dévoilée : Non dévoilée")


affichage_menu()
jeu()
