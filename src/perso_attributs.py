from Lecteur import AnalyseTexte
from collections import defaultdict, Counter


class AnalyseurPersonnages:

    def __init__(self):
        self.attributs_personnages = defaultdict(list)


    def trouver_attributs(self, dico_perso : AnalyseTexte | dict, doc : Doc) -> dict:

        personnages = list(dico_perso.keys())
        for perso in personnages:
            liste_compl = [
                token.lemma_ for token in doc
                if token.head.text == perso and token.dep_ == "amod"
            ]
            liste_red = [att for att, _ in Counter(liste_compl).most_common(3)]
            self.attributs_personnages[perso] = liste_red

        return self.attributs_personnages
