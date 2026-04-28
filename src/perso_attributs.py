from lecteur import AnalyseTexte
from collections import defaultdict, Counter


class AnalyseurPersonnages:

    def __init__(self, dico_perso : AnalyseTexte | dict, doc : Doc):
        self.dico_perso = dico_perso
        self.doc = doc
        self.personnages = list(self.dico_perso.keys())
        self.attributs_personnages = defaultdict(list)


    def trouver_attributs(self) -> dict:

        for perso in self.personnages:
            liste_compl = [
                token.lemma_ for token in self.doc
                if token.head.text == perso and token.dep_ == "amod"
            ]
            liste_red = list(Counter(liste_compl).most_common(3).keys())
            self.attributs_personnages[perso] = liste_red

        return self.attributs_personnages
