import re
from abc import ABC, abstractmethod
from importateur import Texte


class LecteurTexte(ABC):
    """classe parente et abstraite d'analyse d'un texte"""
    @abstractmethod
    def lecture(self, texte: Texte):
        pass


class DecoupeMots(LecteurTexte):
    """retourne la liste de tous les mots du texte"""
    def lecture(self, texte: Texte) -> list:
        resultat = re.sub(r"[\s\W]+", " ", texte.contenu).split()
        return resultat

class DecoupePhrases(LecteurTexte):
    """retourne la liste de toutes les phrases du texte"""
    def lecture(self, texte: Texte) -> list:
        resultat = texte.contenu.split(". ")
        return resultat




