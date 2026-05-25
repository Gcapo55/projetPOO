"""
Classe AnalyseTexte qui utilise spaCy pour extraire et dédoublonner personnages (PER),
lieux (LOC/GPE) et événements (phrase contenant date/heure et lieu) depuis un Doc,
en filtrant les entités sous un seuil minimal d'occurrences.
"""

from spacy.tokens import Doc

from entite import Evenement, Lieu, Personnage
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

    def __init__(self) -> None:
        self.personnages: list[Personnage] = []
        self.lieux: list[Lieu] = []
        self.evenements: list[Evenement] = []

        self._liste_noms_perso: list[str] = []
        self._liste_noms_lieux: list[str] = []

    def _ajouter_personnage(self, nom: str, doc: Doc) -> None:
        """Stocke tous nouveaux personnages dans la liste de la classe,
        et lance les fonctions d'analyse sur le personnage;
         compte les occurrences."""
        if nom not in self._liste_noms_perso:
            self.personnages.append(
                Personnage(nom, trouver_attributs(nom, doc), trouver_genre(nom, doc))
            )
            self.personnages[-1].compter()
            self._liste_noms_perso.append(nom)
        else:
            self.personnages[self._liste_noms_perso.index(nom)].compter()

    def _ajouter_lieu(self, nom: str, categorie: str) -> None:
        """Stocke tous nouveaux lieux dans la liste de la classe,
        et lance les fonctions d'analyse sur le lieu;
        compte les occurrences."""
        if nom not in self._liste_noms_lieux:
            self.lieux.append(Lieu(nom, categorie))
            self.lieux[-1].compter()
            self._liste_noms_lieux.append(nom)
        else:
            self.lieux[self._liste_noms_lieux.index(nom)].compter()

    def _ajouter_events(self, doc: Doc) -> None:
        """Détecte un lieu, une date et l'heure dans une phrase et
        crée un événement dont le nom de l'objet est la phrase en question."""

        for sent in doc.sents:
            lieu_obj = None
            participants = []
            for ent in sent.ents:
                lieu = trouver_lieu(ent.text, self.lieux)
                if lieu:
                    lieu_obj = lieu
                participants.extend(trouver_participants(ent.text, self.personnages))
            date = trouver_date(sent.text)
            heure = trouver_heure(sent.text)

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
        for ent in doc.ents:
            if ent.label_ == "PER" and not (
                len(ent) == 1
                and (
                    "Title" in ent[0].morph.get("NameType", [])
                    or ent[0].text.lower() in titres_seuls
                )
            ):
                self._ajouter_personnage(nettoyer(ent.text), doc)

            elif ent.label_ in ["LOC", "GPE"]:
                self._ajouter_lieu(nettoyer(ent.text), ent.label_)

        self.personnages = [p for p in self.personnages if p.occurrences >= min_occ]
        self.lieux = [lieu for lieu in self.lieux if lieu.occurrences >= min_occ]

        self._liste_noms_perso = [p.nom for p in self.personnages]
        self._liste_noms_lieux = [lieu.nom for lieu in self.lieux]

        self._ajouter_events(doc)
