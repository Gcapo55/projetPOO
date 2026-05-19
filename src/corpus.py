from dataclasses import dataclass, field


@dataclass
class Corpus:
    """Classe parente qui définit toutes les entités d'un texte"""
    nom: str
    occurrences: int = field(default=0, init=False)

    def compter(self) -> None:
        self.occurrences += 1

@dataclass
class Personnage(Corpus):
    """Définit les personnages d'un texte"""
    attributs: list[str]
    genre: str | None = None


@dataclass
class Lieu(Corpus):
    """Définit les lieux d'un texte"""
    categorie: str | None = None


@dataclass
class Evenement(Corpus):
    """Définit les évènements d'un texte"""
    date: str | None = None
    heure: str | None = None
    lieu: Lieu | None = None
    participants: list[Personnage] = field(default_factory=list)

    def __str__(self) -> str:
        """Fonction de print() utile à nos tests"""
        nom_lieu = self.lieu.nom if self.lieu else "N/A"

        return (f"Évenement :"
                f"nom={' '.join(self.nom.split()[:5])} ...,"
                f"date={self.date or 'N/A'},"
                f"heure={self.heure or 'N/A'},"
                f"lieu={nom_lieu},"
                f"participants={', '.join(p.nom for p in self.participants) or 'N/A'}"
        )
