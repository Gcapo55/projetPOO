"""
Fonctions utilitaires pour extraire les métadonnées d'un événement :
résolution du lieu et des participants par correspondance avec
les listes existantes, et détection de la date et de l'heure
via expressions régulières.
"""

import re

from entite import Lieu, Personnage


def trouver_lieu(texte: str, liste_lieux: list[Lieu]) -> Lieu | None:
    """Détérmine si le lieu d'un évenement
    appartient à la liste des lieux"""
    for lieu in liste_lieux:
        if lieu.nom == texte:
            return lieu
    return None


def trouver_participants(texte: str, liste_perso: list[Personnage]) -> list[Personnage]:
    """Détérmine si les participants d'un événement
    font partie de la liste des personnages, retourne
    ces participants"""
    return [p for p in liste_perso if p.nom == texte]


def trouver_date(texte: str) -> str | None:
    """Détermine la date de l'événement"""
    match_date = re.compile(
        r"\b\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet"
        r"|août|septembre|octobre|novembre|décembre)(\s+\d{4})?\b"
        r"|(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)"
        r"|\b(en\s+)?\d{4}\b",
        re.IGNORECASE,
    ).search(texte)
    if match_date:
        return match_date.group()
    return None


def trouver_heure(texte: str) -> str | None:
    """Détermine l'heure de l'événement"""
    match_heure = re.compile(
        r"\b([01]?\d|2[0-3])h([0-5]\d)?\b"
        r"|\b([01]?\d|2[0-3]):[0-5]\d\b"
        r"|\b(midi|minuit)\b"
        r"|\b(matin|soir|après-midi)\b",
        re.IGNORECASE,
    ).search(texte)
    if match_heure:
        return match_heure.group()
    return None
