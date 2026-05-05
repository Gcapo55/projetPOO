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
        liste_perso = self._finder.personnages
        liste_lieu = self._finder.lieux
        liste_evenements = self._finder.evenements
        print(liste_perso)
        print(liste_lieu)
        print(*liste_evenements, sep="\n")


if __name__ == "__main__" :

    pipeline = Pipeline("../docs/L'imposture.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
