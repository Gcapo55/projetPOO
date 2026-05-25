"""Lecteur de texte"""  # noqa: N999 disable invalid module name

from spacy.tokens import Doc

from corpus import Evenement, Lieu, Personnage
from Finder import Finder
from fonction_perso import (
    trouver_attributs,
    trouver_genre,
)
from fonctions_evenement import (
    trouver_date,
    trouver_heure,
    trouver_lieu,
    trouver_participants,
)
from utils import nettoyer

titres_seuls = {"monsieur", "madame", "mme", "m.", "mr"}


class AnalyseTexte:
    """Utilise spaCy pour extraire les personnages, les lieux,
    et les événements, les stocke dans une liste d'instances"""

    def __init__(self):
        self.personnages = []
        self.lieux = []
        self.evenements = []

    def _ajouter_personnage(self, noms: dict, doc: Doc) -> None:
        """Stocke tous nouveaux personnages dans la liste de la classe,
        et lance les fonctions d'analyse sur le personnage;
         compte les occurrences."""
        for nom, occ in noms.items():
            obj = Personnage(nom, trouver_attributs(nom, doc), trouver_genre(nom, doc))
            obj.compter(occ)
            self.personnages.append(obj)


    def _ajouter_lieu(self, noms: dict) -> None:
        """Stocke tous nouveaux lieux dans la liste de la classe,
        et lance les fonctions d'analyse sur le lieu;
        compte les occurrences."""
        for nom, occ in noms.items():
            obj = Lieu(nom, None)
            obj.compter(occ)
            self.lieux.append(obj)


    def _ajouter_events(self, doc: Doc) -> None:
        """Détecte un lieu, une date et l'heure dans une phrase et
        crée un événement dont le nom de l'objet est la phrase en question."""

        for sent in doc.sents:
            # Itère chaque phrase du texte
            # Trouve les attributs d'un éventuel événement
            lieu_obj = None
            participants = []
            for ent in sent.ents:
                lieu = trouver_lieu(ent.text, self.lieux)
                if lieu:
                    lieu_obj = lieu
                participants.extend(trouver_participants(ent.text, self.personnages))
            date = trouver_date(sent.text)
            heure = trouver_heure(sent.text)

            # Ajoute, s'il existe, l'événement à la liste
            if (date or heure) and lieu_obj:
                nom = nettoyer(sent.text.strip())

                self.evenements.append(
                    Evenement(
                        nom=nom,
                        date=date,
                        heure=heure,
                        lieu=lieu_obj,
                        participants=participants,
                    )
                )

    def analyser(self, doc: Doc, min_occ: int) -> None:
        """Analyse le Doc récupéré de l'importateur en
        appelant les fonctions ajouter."""
        finder = Finder(doc, min_occ)
        finder.find()
        self._ajouter_personnage(finder.liste_perso, doc)
        self._ajouter_lieu(finder.liste_lieux)
        self._ajouter_events(doc)
