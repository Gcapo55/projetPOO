import re

def trouver_date(texte: str) :
    match_date = re.compile(
        r"\b\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet"
        r"|août|septembre|octobre|novembre|décembre)(\s+\d{4})?\b"
        r"|(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)"
        r"|\b(en\s+)?\d{4}\b",
        re.IGNORECASE
    ).search(texte)
    if match_date:
        return match_date.group()