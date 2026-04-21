import re
from abc import ABC, abstractmethod
from texte import Texte


class LecteurTexte(ABC):
    @abstractmethod
    def lecture(self, texte: Texte):
        pass


class DecoupeMots(LecteurTexte):
    def lecture(self, texte: Texte) -> list:
        resultat = re.sub(r"[\s\W]+", " ", texte.contenu).split()
        return resultat




