"""importe la classe Texte"""

class Texte:
    """objet Texte"""

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self._auteur = auteur
        self.contenu = contenu

        self.annee = annee
