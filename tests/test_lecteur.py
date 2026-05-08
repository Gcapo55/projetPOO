import pytest

def test_nombre_personnages(liste_perso):
    """Vérifie qu'on a bien trouvé au moins un personnage."""
    assert len(liste_perso) > 0

def test_type_personnage(liste_perso):
    """Vérifie que ce sont bien des instances de Personnage."""
    from corpus import Personnage
    for perso in liste_perso:
        assert isinstance(perso, Personnage)

@pytest.mark.parametrize("nom_attendu", [
    ("Ned Land"), ("Mr Aronnax")  # Liste des noms attendus dans ton texte de test
])
def test_presence_personnage(liste_perso, nom_attendu):
    """Vérifie qu'un personnage spécifique est présent."""
    noms = [p.nom for p in liste_perso]
    assert nom_attendu in noms