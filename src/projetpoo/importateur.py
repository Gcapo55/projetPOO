"""importe la classe Texte"""

class Texte: # noqa : PLW1641 //the class doesn't implement the "__hash__" method
    """objet Texte"""

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self._auteur = auteur
        self.contenu = contenu

        self._annee = annee

    def __str__(self) -> str:
        return f"{self._titre} ({self._auteur}, {self._annee})"

    def __repr__(self) -> str:
        return (
            f"Texte(titre = {self._titre!r})"
            f"auteur = {self._auteur!r}, année = {self._annee}"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Texte):
            return False
        return self._titre == other._titre and self._auteur == other._auteur

    def __lt__(self, other):
        if not isinstance(other, Texte):
            return False
        return self._annee < other._annee
