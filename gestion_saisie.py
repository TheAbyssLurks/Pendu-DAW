def gestion_saisie(partie):
    saisie = input("Votre choix : ")

    if saisie == "indice" and partie.indice_utiliser is False:
        partie.indice_utiliser = True
        return saisie
    elif saisie == "indice" and partie.indice_utiliser is True:
        print("Vous avez déjà utiliser l'indice pour cette partie.")
    elif saisie == "devoiler" and partie.lettre_devoilee is False:
        partie.lettre_devoilee = True
        return saisie
    elif saisie == "devoiler" and partie.lettre_devoilee is True:
        print("Vous avez déjà dévoilé une lettre")
    else:
        if saisie.isalpha() and len(saisie) == 1:
            if partie.lettre_utilisees.count(saisie) == 0:
                partie.lettre_utilisees.append(saisie)
                partie.lettre_utilisees.sort()
                if partie.mot_rechercher.count(saisie) == 0:
                    return False
                else:
                    return True
            else:
                print("Vous avez déjà entré cette lettre")
                return "dejaentree"
        elif saisie.isalpha() and len(saisie) != 1:
            print("Vous devez saisir une seule lettre")
            return saisie
        else:
            return False
