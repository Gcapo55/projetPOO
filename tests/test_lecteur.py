import pytest

from corpus import Personnage, Lieu, Evenement

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

"""Tests évènements"""

def test_type_evenement(dico_evenements):
    """Vérifie que ce sont bien des instances de Evenement."""
    for event in dico_evenements:
        assert isinstance(event, Evenement)

def test_evenement_a_une_date_ou_heure(dico_evenements):
    """Un évènement doit avoir au moins une date ou une heure."""
    for event in dico_evenements:
        assert event.date is not None or event.heure is not None

def test_presence_lieu_evenement(dico_evenements):
    """Vérifie que Paris est associé à un évènement."""
    lieux = [event.lieu.nom for event in dico_evenements]

    assert "Paris" in lieux

def test_presence_participant(dico_evenements):
    """Vérifie que Ned Land participe à un évènement."""
    participants = []

    for event in dico_evenements:
        participants.extend([p.nom for p in event.participants])

    assert "Ned Land" in participants