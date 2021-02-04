lettreutilisee = []

def gestion_saisie(saisie, mot_rechercher):
    if saisie == "indice" or saisie == "devoiler":

    else:
        if saisie.isalpha() and len(saisie) == 1:

        if saisie.isalpha() and len(saisie) != 1:
            print("Vous devez saisir une seule lettre")



def verification_lettre(mot, saisie):
    if saisie.isalpha() and len(saisie) == 1:
        if saisie in lettreutilisee:
            print("Vous avez déjà utilisé cette lettre.")
        else:
            lettreutilisee.append(saisie)
            lettreutilisee.sort()
            if mot.count(saisie) > 0:
                return True
            else:
                return False
    else:
        print("Vous devez saisir une lettre.")
        return None
