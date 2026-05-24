"""test de classe Exportateur"""

from pathlib import Path

from exportateur import Exportateur


def test_exportateur(liste_perso, liste_lieux, liste_evenements) -> None:
    exportateur = Exportateur(liste_perso, liste_lieux, liste_evenements)
    exportateur.exporter_personnages()
    exportateur.exporter_lieux()
    exportateur.exporter_evenements()
    exportateur.exporter_json()
    assert Path("docs/personnages.csv").exists()
    assert Path("docs/lieux.csv").exists()
    assert Path("docs/evenements.csv").exists()
    assert Path("docs/donnees.json").exists()
