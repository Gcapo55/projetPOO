"""test de classe Texte"""

from importateur import ChargeurTexte, Texte

CONST_ANNEE = "1869"

CHEMIN = "./docs/20'000 lieux sous les mers.txt"


def test_texte_annee(texte_test):
    assert texte_test.annee() == CONST_ANNEE

def test_texte_auteur(texte_test):
    assert texte_test.auteur() == "Jules Verne"

def test_texte_titre(texte_test):
    assert texte_test.titre() == "20'000 lieux sous les mers"

def test_charger():
    charge = ChargeurTexte()
    mille_lieux = charge.charger(CHEMIN)
    assert mille_lieux.auteur() == "Jules Verne"
