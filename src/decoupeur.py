
from abc import ABC, abstractmethod


class DecoupeurTexte(ABC):
    """classe parente et abstraite d'analyse d'un texte"""
    @abstractmethod
    def lecture(self, doc: Doc):
        pass


class DecoupeMots(DecoupeurTexte):
    """retourne la liste de tous les mots du texte : fonction spacy"""
    def lecture(self, doc: Doc) -> list:
        return [token.text for token in doc]

class DecoupePhrases(DecoupeurTexte):
    """retourne la liste de toutes les phrases du texte : fonction spacy"""
    def lecture(self, doc: Doc) -> list:
        return [token.sent for token in doc.sents]




