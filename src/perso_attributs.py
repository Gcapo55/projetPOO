from Lecteur import AnalyseTexte
from collections import defaultdict, Counter


class AnalyseurPersonnages:

    def __init__(self, dico_perso : AnalyseTexte | dict, txt_src : Doc):
        self.dico_perso = dico_perso
        self.txt_src = txt_src
        self.personnages = list(self.source.keys())
        self.attributs_personnages = defaultdict(list)


    def trouver_attributs(self) -> dict:

        for perso in self.personnages:
            liste_compl = [
                token.lemma_ for token in self.txt_src
                if token.head.text == perso and token.dep_ == "amod"
            ]
            liste_red = list(Counter(liste_compl).most_common(3).keys())
            self.attributs_personnages[perso] = liste_red

        return self.attributs_personnages
