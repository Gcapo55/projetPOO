"""Trouve les personnages et lieux principaux d'un texte littéraire"""

from collections import Counter
from spacy.tokens import Doc


class Finder:
    def __init__(self, doc: Doc, min_occ) -> None:
        self._doc = doc
        self._min_occ = min_occ

        self.liste_perso = []
        self.liste_lieux = []

        self._titres_seuls = {"monsieur", "madame", "mme", "m.", "mr"}

    def find(self) -> dict:
        """Stocke dans des listes de la classe,
        les personnages et lieux principaux."""
        tot_perso = []
        tot_lieux = []

        for ent in self._doc.ents:
            if ent.label_ == "PER" and not (
                len(ent) == 1
                and (
                    "Title" in ent[0].morph.get("NameType", [])
                    or ent[0].text.lower() in self._titres_seuls
                )
            ):
                tot_perso.append(ent.text)

            elif ent.label_ in ["LOC", "GPE"]:
                tot_lieux.append(ent.text)

        counter_perso = Counter(tot_perso)
        counter_lieux = Counter(tot_lieux)

        self.liste_perso = Counter(
            {k: v for k, v in counter_perso.items() if v > self._min_occ}
        )
        self.liste_lieux = Counter(
            {k: v for k, v in counter_lieux.items() if v > self._min_occ}
        )
