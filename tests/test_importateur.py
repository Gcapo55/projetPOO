"""test de classe Texte"""

from importateur import Texte

TexteTest = Texte("Le Bon, la Brute et le Truand", "Joseph Morrington", """Le Bon
                   a vu la Brute et le Truand s'entretuer""", 1957)

CONST_ANNEE = 1957

def test_texte_annee():
    assert TexteTest.annee() == CONST_ANNEE

def test_texte_auteur():
    assert TexteTest.auteur() == "Joseph Morrington"

def test_texte_titre():
    assert TexteTest.titre() == "Le Bon, la Brute et le Truand"
