from collections import Counter

from spacy.tokens import Doc

from utils import nettoyer


def trouver_attributs(nom: str, doc : Doc) -> list:
    """Détérmine les 3 adjectifs les plus associés à chaque personnage"""
    liste_compl = [
             nettoyer(token.lemma_) for token in doc
             if token.head.text == nom and token.dep_ == "amod"
         ]
    return [att for att, _ in Counter(liste_compl).most_common(3)]

def trouver_genre(nom: str, doc : Doc) -> str:
    """Détérmine le genre d'un personnage"""
    liste_compl = [
        "".join(token.morph.get("Gender")) for token in doc
        if token.text == nom
    ]
    if liste_compl:
        return Counter(liste_compl).most_common(1)[0][0]
    else:
        return None