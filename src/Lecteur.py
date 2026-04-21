import spacy
import fr_core_news_sm
from corpus import *

nlp = fr_core_news_sm.load()

texte = """
Henry allait au marché à Nice et se baladait au bord du port avec Sophie. Pour que Matthias, Matthias puisse les rejoindre, il envoya son adresse à sa maman qui habite à Lausanne. C'était Carnaval.
Ils ont fini par rejoindre Jean.
"""

class AnalyseTexte:
    def __init__(self, nlp):
        self.nlp = nlp
        self.personnages = {}
        self.lieux = {}

    def analyser(self, texte):
        doc = self.nlp(texte)

        for ent in doc.ents:
            if ent.label_ == "PER":
                self._ajouter_personnage(ent.text)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(ent.text)

    def _ajouter_personnage(self, nom):
        if nom not in self.personnages:
            self.personnages[nom] = Personnage(nom)
        self.personnages[nom].compter()

    def _ajouter_lieu(self, nom):
        if nom not in self.lieux:
            self.lieux[nom] = Lieu(nom)
        self.lieux[nom].compter()

if __name__ == "__main__":
    analyse = AnalyseTexte(nlp)
    analyse.analyser(texte)

    print(analyse.personnages)
    print(analyse.lieux)
