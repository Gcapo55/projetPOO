"""test de classe Texte + Importateur"""

from importateur import ChargeurTexte

CHEMIN = "./docs/ArseneLupin.txt"


def test_charger():
    charge = ChargeurTexte()
    mille_lieux = charge.charger(CHEMIN)
    assert mille_lieux.auteur() == "Jules Verne"
    assert "vingt mille lieues sous les mers" in mille_lieux.titre().lower()
    assert mille_lieux.annee().lower() in ["1869", None]
