class Partie:

    def __init__(self, etat, nberreurs, indiceutiliser, lettredevoilee, mottrouver):
        self.etat = etat
        self.nberreurs = nberreurs
        self.indiceutiliser = indiceutiliser
        self.lettredevoilee = lettredevoilee
        self.mottrouver = mottrouver

    def gestion_partie(self):
        if self.nberreurs < 6:
            self.nberreurs += 1
        elif self.nberreurs >= 6:
            self.etat = 2

    def utilisation_indice(self):
        self.indiceutiliser = True

    def utilisation_lettre(self):
        self.lettredevoilee = True

    def verification_mot(self, motrechercher, lettreutilisee):
        if len(lettreutilisee) >= len(motrechercher):
            resultat = all(lettre in motrechercher for lettre in lettreutilisee)
            if resultat:
                self.etat = 1
