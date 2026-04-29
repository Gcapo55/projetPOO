"""Lecteur de texte"""  # noqa: N999 disable invalid module name
import re

from spacy.tokens import Doc

from corpus import Evenement, Lieu, Personnage

from utils import nettoyer

from perso_attributs import trouver_attributs

from analyse_events import trouver_date

min_occ = 10

class AnalyseTexte:
    """ Utilise spaCy pour extraire les personnages et les lieux,
    les stocke dans un dictionnaire et les attribue à la classe correspondante. """
    def __init__(self):
        self.personnages = []
        self.lieux = []
        self.evenements = {}

    def _ajouter_personnage(self, nom: str, doc: Doc ):
        """ Stocke tous nouveaux personnages dans la liste de la classe,
        et lance les fonctions d'analyse sur le personnage;
         compte les occurrences. """
        liste_noms = [x.nom for x in self.personnages]
        if nom not in liste_noms:
            self.personnages.append(
                Personnage(nom,
                           trouver_attributs(nom, doc),
                           None)
            )
            self.personnages[-1].compter()
        else : self.personnages[liste_noms.index(nom)].compter()


    def _ajouter_lieu(self, nom: str, doc: Doc):
        """ Stocke tous nouveaux lieux dans la liste de la classe,
        et lance les fonctions d'analyse sur le lieu;
        compte les occurrences. """
        liste_lieux = [x.nom for x in self.lieux]
        if nom not in liste_lieux:
            self.lieux.append(
                Lieu(nom,
                     None)
            )
            self.lieux[-1].compter()
        else : self.lieux[liste_lieux.index(nom)].compter()

    def _ajouter_events(self, doc : Doc) -> dict:
        """ Détecte un lieu, une date et l'heure dans une phrase et
        crée un évenement dont le nom de l'objet est la phrase en question. """

        for sent in doc.sents:
            date = None
            heure = None
            lieu_obj = None
            participants = []

            for ent in sent.ents:
                for l in self.lieux:
                    if ent.text == l.nom:
                        lieu_obj = l
                for p in self.personnages:
                    if ent.text == p.nom:
                        participants.append(p)

            date = trouver_date(sent.text)

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
                nom = nettoyer(sent.text.strip())
                if nom not in self.evenements:
                    self.evenements[nom] = Evenement(
                        nom=nom,
                        date=date,
                        heure=heure,
                        lieu=lieu_obj,
                        personnages=participants,
                    )


    def analyser(self, doc : Doc) -> dict:
        """ Attribue le texte récupéré de l'importateur et
        appelle les fonctions ajouter. """
        for ent in doc.ents:
            if ent.label_ == "PER":
                self._ajouter_personnage(nettoyer(ent.text), doc)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(nettoyer(ent.text), doc)

        self.personnages = [p for p in self.personnages if p.occurences >= min_occ]
        self.lieux = [l for l in self.lieux if l.occurences >= min_occ]

        # for nom_lieu, obj_lieu in list(self.lieux.items()):
        #     if obj_lieu.occurences < min_occ :
        #         del self.lieux[nom_lieu]




        self._ajouter_events(doc)


