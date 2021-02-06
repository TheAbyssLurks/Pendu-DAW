# Classe contenant toutes les informations d'une partie.
class Partie:

    def __init__(self, etat, nb_erreurs, indice_utiliser, lettre_devoilee, mot_rechercher, mot_trouver, indice):
        self.etat = etat
        self.nb_erreurs = nb_erreurs
        self.indice_utiliser = indice_utiliser
        self.lettre_devoilee = lettre_devoilee
        self.mot_rechercher = mot_rechercher
        self.mot_trouver = mot_trouver
        self.indice = indice
        self.lettre_indice = ""
        self.lettre_utilisees = []

    # Fonction qui permet de gérer les erreurs.
    def gestion_erreurs(self):
        self.nb_erreurs += 1
        if self.nb_erreurs == 6:
            self.etat = 2

    # Fonction qui permet de modifier la valeur mot_trouver pour y ajouter les lettres trouvées.
    def modification_mot_trouver(self):
        for lettre in self.lettre_utilisees:
            if self.mot_rechercher.count(lettre) > 0:
                index = self.mot_rechercher.index(lettre)
                self.mot_trouver[index] = lettre
    #
    # Fonction qui permet de gérer le dévoilement des lettres de la variable
    # def devoilement_mot_trouver(self):
    #     for lettre in self.lettre_utilisees:
    #         index = self.mot_rechercher.index(lettre)
    #         self.mot_trouver[index] = lettre

    # Fonction qui permet de gérer le dévoilement d'une lettre.
    def devoilement_lettre(self):
        if self.lettre_devoilee is True:
            index = self.mot_trouver.index("_")
            self.mot_trouver[index] = self.mot_rechercher[index]
            self.lettre_indice += self.mot_rechercher[index]
            self.lettre_utilisees.append(self.lettre_indice)
        else:
            return

    # Fonction qui permet de vérifier si le mot_rechercher à été trouvé.
    def verification_mot(self):
        if len(self.lettre_utilisees) >= len(self.mot_rechercher):
            resultat = all(lettre in self.mot_rechercher for lettre in self.lettre_utilisees)
            if resultat:
                self.etat = 1
