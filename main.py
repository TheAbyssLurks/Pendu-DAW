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
    nouvelle_partie = moteur_jeu.Partie(0, -1, False, False, False)

affichage_menu()
