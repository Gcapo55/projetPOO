import re
from corpus import Lieu, Personnage


def trouver_lieu(texte: str, liste_lieux: list[Lieu]) -> Lieu|None:
    """Détérmine si le lieu d'un évenement
    appartient à la liste des lieux"""
    for lieu in liste_lieux:
        if lieu.nom == texte:
            return lieu
    return None

def trouver_participants(texte: str, liste_perso: list[Personnage]) -> list[Personnage]:
    """Détérmine si les participants d'un événement
    font partie de la liste des personnages"""
    participants = []
    for p in liste_perso:
        if p.nom == texte:
            participants.append(p)
    return participants

def trouver_date(texte: str) -> str|None :
    """Détérmine la date de l'événement"""
    match_date = re.compile(
        r"\b\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet"
        r"|août|septembre|octobre|novembre|décembre)(\s+\d{4})?\b"
        r"|(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)"
        r"|\b(en\s+)?\d{4}\b",
        re.IGNORECASE
    ).search(texte)
    if match_date:
        return match_date.group()
    return None

def trouver_heure(texte: str) -> str|None:
    """Détérmine l'heure de l'événement"""
    match_heure = re.compile(
                    r"\b([01]?\d|2[0-3])h([0-5]\d)?\b"
                    r"|\b([01]?\d|2[0-3]):[0-5]\d\b"
                    r"|\b(midi|minuit)\b"
                    r"|\b(matin|soir|après-midi)\b",
                    re.IGNORECASE
                ).search(texte)
    if match_heure:
        return match_heure.group()
    return None