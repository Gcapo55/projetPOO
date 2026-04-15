from abc import ABC, abstractmethod
from texte import Texte


class LecteurTexte(ABC) :
    @abstractmethod
    def lecture (self, texte : Texte) :
        pass
    
