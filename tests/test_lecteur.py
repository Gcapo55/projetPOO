import pytest

from corpus import Evenement, Lieu


@pytest.mark.parametrize(
    "perso_attendus",
    [
        ("Ned Land"),
        ("Mr Aronnax"),  # Liste des noms attendus dans ton texte de test
    ],
)
def test_presence_personnage(liste_perso, perso_attendus):
    """Vérifie qu'un personnage spécifique est présent."""
    noms = [p.nom for p in liste_perso]
    assert perso_attendus in noms


"""Test lieux"""


def test_nombre_personnages(liste_lieux):
    """Vérifie qu'on a bien trouvé au moins un lieu."""
    assert len(liste_lieux) > 0


def test_type_personnage(liste_lieux):
    """Vérifie que ce sont bien des instances de Lieu."""
    for perso in liste_lieux:
        assert isinstance(perso, Lieu)


@pytest.mark.parametrize(
    "lieux_attendus",
    [
        ("Paris"),  # Liste des lieux attendus dans ton texte de test
    ],
)
def test_presence_lieux(liste_lieux, lieux_attendus):
    """Vérifie qu'un lieu spécifique est présent."""
    noms = [p.nom for p in liste_lieux]
    assert lieux_attendus in noms


"""Tests évènements"""


def test_type_evenement(liste_evenements):
    """Vérifie que ce sont bien des instances de Evenement."""
    for event in liste_evenements:
        assert isinstance(event, Evenement)


def test_evenement_a_une_date_ou_heure(liste_evenements):
    """Un évènement doit avoir au moins une date ou une heure."""
    for event in liste_evenements:
        assert event.date is not None or event.heure is not None


def test_presence_lieu_evenement(liste_evenements):
    """Vérifie que Paris est associé à un évènement."""
    lieux = [event.lieu.nom for event in liste_evenements]

    assert "Paris" in lieux


def test_presence_participant(liste_evenements):
    """Vérifie que Ned Land participe à un évènement."""
    participants = []

    for event in liste_evenements:
        participants.extend([p.nom for p in event.participants])

    assert "Ned Land" in participants
