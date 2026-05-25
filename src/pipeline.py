import installation_spacy  # pylint: disable=unused-import  # noqa: F401
from exportateur import Exportateur
from importateur import ChargeurTexte
from Lecteur import AnalyseTexte
from utils import patienter, spacy_conv, terminer


class Pipeline:
    """Classe qui fait fonctionner toute l'architecture
    du projet (import, analyse, export)"""
    def __init__(self,
                 source : str,
                 chargeur : ChargeurTexte,
                 finder : AnalyseTexte
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
        exportateur = Exportateur(liste_perso, liste_lieu, liste_evenements)
        exportateur.exporter_personnages()
        exportateur.exporter_lieux()
        exportateur.exporter_evenements()
        exportateur.exporter_json()
        terminer()


if __name__ == "__main__" :
    inp = str(input("Quel est le nom du fichier à analyser ? : ")
               or "20'000 lieux sous les mers.txt")
    pipeline = Pipeline(inp,
                    ChargeurTexte(),
                    AnalyseTexte(),
                    )

    pipeline.executer()
