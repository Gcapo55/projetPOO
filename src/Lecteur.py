"""Lecteur de texte"""  # noqa: N999 disable invalid module name
import re

from spacy.tokens import Doc

from corpus import Evenement, Lieu, Personnage


class AnalyseTexte:
    """ Utilise spaCy pour extraire les personnages et les lieux,
    les stocke dans un dictionnaire et les attribue à la classe correspondante. """
    def __init__(self):
        self.personnages = {}
        self.lieux = {}
        self.evenements = {}

    def _ajouter_personnage(self, nom):
        """ Stocke les personnages dans le dictionnaire
        et les attribue à la classe correspondante. """
        if nom not in self.personnages:
            self.personnages[nom] = Personnage(nom, None)
        self.personnages[nom].compter()

    def _ajouter_lieu(self, nom):
        """ Stocke les lieux dans le dictionnaire et
        les attribue à la classe correspondante. """
        if nom not in self.lieux:
            self.lieux[nom] = Lieu(nom, None)
        self.lieux[nom].compter()

    def _ajouter_events(self, doc : Doc) -> dict:
        """ Détecte un lieu, une date et l'heure dans une phrase et
        crée un évenement dont le nom de l'objet est la phrase en question. """

        for sent in doc.sents:
            date = None
            heure = None
            lieu_obj = None
            participants = []

            for ent in sent.ents:
                if ent.label_ in ["LOC", "GPE"]:
                    lieu_obj = self.lieux.get(ent.text) # lien vers l'objet lieu
                elif ent.label_ == "PER":
                    p = self.personnages.get(ent.text)
                    if p:
                        participants.append(p)

            match_date = re.compile(
                r"\b\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet"
                r"|août|septembre|octobre|novembre|décembre)(\s+\d{4})?\b"
                r"|(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)"
                r"|\b(en\s+)?\d{4}\b",
                re.IGNORECASE
            ).search(sent.text)
            if match_date:
                date = match_date.group()

            match_heure = re.compile(
                r"\b([01]?\d|2[0-3])h([0-5]\d)?\b"
                r"|\b([01]?\d|2[0-3]):[0-5]\d\b"
                r"|\b(midi|minuit)\b"
                r"|\b(matin|soir|après-midi)\b",
                re.IGNORECASE
            ).search(sent.text)
            if match_heure:
                heure = match_heure.group()

            if (date or heure) and lieu_obj:
                nom = sent.text.strip()
                if nom not in self.evenements:
                    self.evenements[nom] = Evenement(
                        nom=nom,
                        date=date,
                        heure=heure,
                        lieu=lieu_obj,
                        personnage=participants,
                    )


    def analyser(self, doc : Doc) -> dict:
        """ Attribue le texte récupéré de l'importateur et
        appelle les fonctions ajouter. """
        for ent in doc.ents:
            if ent.label_ == "PER":
                self._ajouter_personnage(ent.text)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(ent.text)

        self._ajouter_events(doc)


