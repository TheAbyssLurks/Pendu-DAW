import random


# Classe contenant les informations du mot rechercher durant la partie.
class Mot_Rechercher:
    def __init__(self, mot, indice):
        self.mot = mot
        self.indice = indice


liste_mot = {"abricot": "Gros fruit charnu, sucré et savoureux, dont le noyau lisse contient une amande comestible "
                        "et dont la pulpe est utilisée en confiturerie et en pâtisserie.",
             "chien": "Animal que l'on surnomme le meilleur ami de l'Homme.",
             "chat": "Mammifère carnivore (félidé), sauvage ou domestique, au museau court et arrondi.",
             "poutine": "Au Canada, mélange de pommes de terre frites et de fromage en grains arrosé de sauce "
                        "chaude.",
             "musique": "Art qui permet à l'Homme de s'exprimer par l'intermédiaire des sons.",
             "sapin": "Conifère (pinacée) des régions tempérées de l'hémisphère Nord.",
             "livre": "Assemblage de feuilles imprimées et réunies en un volume, broché ou relié."
             }


# Fonction qui permet de tirer un mot au hasard.
def tirage_mot(dictionnaire):
    mot = random.choice(list(dictionnaire))
    indice = dictionnaire.get(mot)

    nouveaumot = Mot_Rechercher(mot, indice)
    return nouveaumot
