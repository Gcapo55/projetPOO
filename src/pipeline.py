from importateur import ChargeurTexte
import installation_spacy # pylint: disable=unused-import
from Lecteur import AnalyseTexte
from exportateur import Exportateur
from utils import spacy_conv, patienter


class Pipeline:
    """Classe qui fait fonctionner toute l'architecture
    du projet (import, analyse, export)"""
    def __init__(self,
                 source : str,
                 chargeur : ChargeurTexte,
                 finder : AnalyseTexte,
                 exportateur : Exportateur,
                 ) -> None:
        self.source = source
        self._chargeur = chargeur
        self._finder = finder
        self._exportateur = exportateur

    def executer(self) -> None:
        """Fonction qui fait l'exécution du programme"""
        patienter()
        texte = self._chargeur.charger(self.source)
        doc = spacy_conv(texte)
        self._finder.analyser(doc, 10)
        #liste_perso = self._finder.personnages
        #liste_lieu = self._finder.lieux
        #liste_evenements = self._finder.evenements
        self._exportateur.ExporterPersonnages()
        self._exportateur.ExporterLieux()
        self._exportateur.ExporterEvenements()
        #print(liste_perso)
        #print(liste_lieu)
        #print(*liste_evenements, sep="\n")


if __name__ == "__main__" :

    pipeline = Pipeline("20'000 lieux sous les mers.txt",
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
