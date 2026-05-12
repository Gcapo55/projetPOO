"""test de classe Texte + Importateur"""

from importateur import ChargeurTexte

CHEMIN = "./docs/20'000 lieux sous les mers.txt"


def test_charger():
    charge = ChargeurTexte()
    mille_lieux = charge.charger(CHEMIN)
    assert mille_lieux.auteur() == "Jules Verne"
    assert "vingt mille lieues sous les mers" in mille_lieux.titre().lower()
    assert mille_lieux.annee().lower() in ["1869", "february 1, 2004"]