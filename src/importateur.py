import re
from pathlib import Path


# @dataclass
class Texte:
    """objet Texte"""

    def __init__(self, titre: str, auteur: str, contenu: str, annee: str):
        self._titre = titre
        self._auteur = auteur
        self.contenu = contenu

        self._annee = annee

    def __str__(self) -> str:
        return f"{self._titre} ({self._auteur}, {self._annee})"


    def titre(self) -> str:
        return self._titre
    def annee(self) -> int:
        return self._annee

    def auteur(self) -> str:
        return self._auteur


class ChargeurTexte:
    """lis et crée une instance de Texte"
    "avec un nom de fichier .txt, selon le format importé depuis Projekt Gutenberg"""
    def charger(self, source : str)-> Texte:
        with Path.open(source, "r", encoding="utf-8") as file:
            global_contenu = file.read()
            titre = re.search(r"(?<=Title:\s).+?(?=\n)", global_contenu)
            auteur = re.search(r"(?<=Author:\s).+?(?=\n)", global_contenu)
            contenu = re.search(r"\*\*\*[^*]+\*\*\*(.+?)(?=\*\*\*|$)", global_contenu, re.DOTALL)  # noqa: E501
            date = re.search(r"(?<=Release date:\s).+?([\d]{4})(?=\s)", global_contenu)#mettre "Original Publication :"
            return Texte(titre.group(), auteur.group(), contenu.group(), date.group())
