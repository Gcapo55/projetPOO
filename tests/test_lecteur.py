import pytest

from corpus import Personnage, Lieu

"""Test personnages"""
def test_nombre_personnages(dico_perso):
    """Vérifie qu'on a bien trouvé au moins un personnage."""
    assert len(dico_perso) > 0

def test_type_personnage(dico_perso):
    """Vérifie que ce sont bien des instances de Personnage."""
    for perso in dico_perso:
        assert isinstance(perso, Personnage)

@pytest.mark.parametrize("perso_attendus", [
    ("Ned Land"), ("Mr Aronnax"), # Liste des noms attendus dans ton texte de test
])
def test_presence_personnage(dico_perso, perso_attendus):
    """Vérifie qu'un personnage spécifique est présent."""
    noms = [p.nom for p in dico_perso]
    assert perso_attendus in noms

"""Test lieux"""
def test_nombre_personnages(dico_lieux):
    """Vérifie qu'on a bien trouvé au moins un lieu."""
    assert len(dico_lieux) > 0

def test_type_personnage(dico_lieux):
    """Vérifie que ce sont bien des instances de Lieu."""
    for perso in dico_lieux:
        assert isinstance(perso, Lieu)

@pytest.mark.parametrize("lieux_attendus", [
    ("Paris"), # Liste des lieux attendus dans ton texte de test
])
def test_presence_lieux(dico_lieux, lieux_attendus):
    """Vérifie qu'un lieu spécifique est présent."""
    noms = [p.nom for p in dico_lieux]
    assert lieux_attendus in noms