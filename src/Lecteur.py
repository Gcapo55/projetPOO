import spacy
import fr_core_news_sm
from importateur import Texte
from corpus import *

nlp = fr_core_news_sm.load()

class AnalyseTexte:
    """ Utilise spaCy pour extraire les personnages et les lieux, les stocke dans un dictionnaire et les attribue à la classe correspondante. """
    def __init__(self, nlp):
        self.nlp = nlp
        self.personnages = {}
        self.lieux = {}

    """ Stocke les personnages dans le dictionnaire et les attribue à la classe correspondante. """
    def _ajouter_personnage(self, nom):
        if nom not in self.personnages:
            self.personnages[nom] = Personnage(nom)
        self.personnages[nom].compter()

    """ Stocke les lieux dans le dictionnaire et les attribue à la classe correspondante. """
    def _ajouter_lieu(self, nom):
        if nom not in self.lieux:
            self.lieux[nom] = Lieu(nom)
        self.lieux[nom].compter()

    """ Attribue le texte récupéré de l'importateur et appelle les fonctions ajouter. """
    def analyser(self, texte : Texte):
        doc = self.nlp(texte.contenu)

        for ent in doc.ents:
            if ent.label_ == "PER":
                self._ajouter_personnage(ent.text)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(ent.text)

