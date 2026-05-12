import pytest

from corpus import Personnage


def test_nombre_personnages(dico_perso):
    """Vérifie qu'on a bien trouvé au moins un personnage."""
    assert len(dico_perso) > 0

def test_type_personnage(dico_perso):
    """Vérifie que ce sont bien des instances de Personnage."""
    for perso in dico_perso:
        assert isinstance(perso, Personnage)

@pytest.mark.parametrize("nom_attendu", [
    ("Pablo"),  # Liste des noms attendus dans ton texte de test
])
def test_presence_personnage(dico_perso, nom_attendu):
    """Vérifie qu'un personnage spécifique est présent."""
    noms = [p.nom for p in dico_perso]
    assert nom_attendu in noms
