
import re
from abc import ABC, abstractmethod

from importateur import Texte


class LecteurTexte(ABC):
    @abstractmethod
    def lecture(self, texte: Texte):
        pass


class DecoupeMots(LecteurTexte):
    def lecture(self, texte: Texte) -> list:
        return re.sub(r"[\s\W]+", " ", texte.contenu).split()




