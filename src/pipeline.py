from utils import *
from perso_attributs import *
from importateur import *

class Pipeline:
    def __init__(self,
                 source : str,
                 chargeur : ChargeurTexte,
                 finder : AnalyseTexte,
                 perso_analyser : AnalyseurPersonnages
                 ):
        self.source = source
        self._chargeur = chargeur
        self._finder = finder
        self._perso_analyser = perso_analyser

    def executer(self):

        texte = self._chargeur.charger(self.source)
        doc = spacy_conv(texte)
        self._finder.analyser(doc)
        dico_perso = self._finder.personnages
        # dico_lieu = self._finder.lieux
        # dico_attributs = self._perso_analyser.trouver_attributs(dico_perso, doc)
        print (list((dico_perso)))
        print (dico_attributs)

if __name__ == "__main__" :

    pipeline = Pipeline("../docs/20'000 lieux sous les mers.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    AnalyseurPersonnages()
                    )

    pipeline.executer()