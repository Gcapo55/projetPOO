from importateur import ChargeurTexte
from Lecteur import AnalyseTexte
from utils import spacy_conv, stanza_conv


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
        doc = stanza_conv(texte)
        lst_words = [word for sent in doc.sentences for word in sent.words]
        self._finder.analyser(doc,lst_words)
        liste_perso = self._finder.personnages
        liste_lieu = self._finder.lieux
        liste_evenements = self._finder.evenements
        print(liste_perso)
        print(liste_lieu)
        print(*liste_evenements, sep="\n")


if __name__ == "__main__" :

    pipeline = Pipeline("../docs/20'000 lieux sous les mers.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
