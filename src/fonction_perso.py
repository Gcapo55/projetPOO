from collections import Counter

from spacy.tokens import Doc

from utils import nettoyer

def check_attribut(nom, tok, doc) :
    """fonction qui utilise les tags de spacy pour vérifier qu'il s'agit d'un adjectif"""
    if tok.text not in nom and tok.head.text not in nom:
        return None
    if tok.text in nom :
        if tok.dep_ == "appos" and tok.head.pos_ == "ADJ":
            return tok.head.text

        elif tok.dep_ == "nsubj" and tok.head.pos_ == "ADJ":
            return tok.head.text

        elif tok.dep_ == "appos" and doc[tok.i - 1].pos_ == "ADJ":
            return doc[tok.i - 1].text

    elif tok.head.text in nom and tok.dep_ == "amod" :
        return tok.text

    else :
        return None

def trouver_attributs(nom: str, doc : Doc) -> list:
    """Détermine les 3 adjectifs les plus associés à chaque personnage"""
    liste_compl = [
        nettoyer(check_attribut(nom,token,doc)) for token in doc
        if check_attribut(nom,token,doc) is not None
    ]

    return [att for att, _ in Counter(liste_compl).most_common(3)]

def trouver_genre(nom: str, doc : Doc) -> str:
    """Détermine le genre d'un personnage"""
    liste_compl = [
        "".join(token.morph.get("Gender")) for token in doc
        if token.text in nom
    ]
    if liste_compl:
        return Counter(liste_compl).most_common(1)[0][0]
    return None
