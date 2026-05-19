import installation_spacy  # pylint: disable=unused-import  # noqa: F401
from importateur import ChargeurTexte
from Lecteur import AnalyseTexte
from utils import patienter, spacy_conv


class Pipeline:
    """Classe qui fait fonctionner toute l'architecture
    du projet (import, analyse, export)"""
    def __init__(self,
                 source : str,
                 chargeur : ChargeurTexte,
                 finder : AnalyseTexte,
                 ) -> None:
        self.source = source
        self._chargeur = chargeur
        self._finder = finder

    def executer(self) -> None:
        """Fonction qui fait l'exécution du programme"""
        patienter()
        texte = self._chargeur.charger(self.source)
        doc = spacy_conv(texte)
        self._finder.analyser(doc, 10)
        liste_perso = self._finder.personnages
        liste_lieu = self._finder.lieux
        liste_evenements = self._finder.evenements
        print(liste_perso)
        print(liste_lieu)
        print(*liste_evenements, sep="\n")


if __name__ == "__main__" :

    pipeline = Pipeline("20'000 lieux sous les mers.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
