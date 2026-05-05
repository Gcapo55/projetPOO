from importateur import ChargeurTexte
from Lecteur import AnalyseTexte
from utils import spacy_conv

class Pipeline:
    def __init__(self,
                 source : str,
                 chargeur : ChargeurTexte,
                 finder : AnalyseTexte,
                 ):
        self.source = source
        self._chargeur = chargeur
        self._finder = finder

    def executer(self):

        texte = self._chargeur.charger(self.source)
        doc = spacy_conv(texte)
        self._finder.analyser(doc)
        dico_perso = self._finder.personnages
        dico_lieu = self._finder.lieux
        dico_evenements = self._finder.evenements
        print(dico_perso)
        print(dico_lieu)
        print(*dico_evenements, sep="\n")


if __name__ == "__main__" :

    pipeline = Pipeline("../docs/20'000 lieux sous les mers.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
