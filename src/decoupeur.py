
import spacy
import re
from abc import ABC, abstractmethod
from importateur import Texte

nlp = spacy.load("fr_core_news_sm")

class LecteurTexte(ABC):
    """classe parente et abstraite d'analyse d'un texte"""
    @abstractmethod
    def lecture(self, texte: Texte):
        pass


class DecoupeMots(LecteurTexte):
    """retourne la liste de tous les mots du texte : fonction spacy"""
    def lecture(self, texte: Texte) -> list:
        resultat = []
        for token in nlp(texte.contenu):
            resultat.append(token.text)
        return resultat

class DecoupePhrases(LecteurTexte):
    """retourne la liste de toutes les phrases du texte : fonction spacy"""
    def lecture(self, texte: Texte) -> list:
        resultat = []
        for token in nlp(texte.contenu).sents:
            resultat.append(token.text)
        return resultat




