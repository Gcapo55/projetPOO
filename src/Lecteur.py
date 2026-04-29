"""Lecteur de texte"""  # noqa: N999 disable invalid module name
import re

from spacy.tokens import Doc

from corpus import Evenement, Lieu, Personnage

from utils import nettoyer

from perso_attributs import trouver_attributs

from analyse_events import trouver_participants, trouver_lieu, trouver_date, trouver_heure

min_occ = 10

class AnalyseTexte:
    """ Utilise spaCy pour extraire les personnages et les lieux,
    les stocke dans un dictionnaire et les attribue à la classe correspondante. """
    def __init__(self):
        self.personnages = []
        self.lieux = []
        self.evenements = []

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
        crée un événement dont le nom de l'objet est la phrase en question. """

        for sent in doc.sents:
            # Itère chaque phrase du texte
            # Trouve les attributs d'un éventuel événement
            lieu_obj = None
            participants = []
            for ent in sent.ents:
                lieu_obj = trouver_lieu(ent.text, self.lieux)
                participants = trouver_participants(ent.text, self.personnages)
            date = trouver_date(sent.text)
            heure = trouver_heure(sent.text)

            #Ajoute, s'il existe, l'événement à la liste
            if (date or heure) and lieu_obj:
                nom = nettoyer(sent.text.strip())

                self.evenements.append(
                    Evenement(
                    nom=nom,
                    date=date,
                    heure=heure,
                    lieu=lieu_obj,
                    participants=participants,
                ))


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

        self._ajouter_events(doc)


