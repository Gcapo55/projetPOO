from corpus import Personnage, Lieu

class AnalyseTexte:
    """ Utilise spaCy pour extraire les personnages et les lieux,
    les stocke dans un dictionnaire et les attribue à la classe correspondante. """
    def __init__(self, doc : Doc):
        self.doc = doc
        self.personnages = {}
        self.lieux = {}

    def _ajouter_personnage(self, nom):
        """ Stocke les personnages dans le dictionnaire
        et les attribue à la classe correspondante. """
        if nom not in self.personnages:
            self.personnages[nom] = Personnage(nom)
        self.personnages[nom].compter()

    def _ajouter_lieu(self, nom):
        """ Stocke les lieux dans le dictionnaire et
        les attribue à la classe correspondante. """
        if nom not in self.lieux:
            self.lieux[nom] = Lieu(nom)
        self.lieux[nom].compter()

    def analyser(self) -> dict:
        """ Attribue le texte récupéré de l'importateur et
        sappelle les fonctions ajouter. """
        for ent in self.doc.ents:
            if ent.label_ == "PER":
                self._ajouter_personnage(ent.text)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(ent.text)

