from dataclasses import dataclass, field

@dataclass
class Corpus:
    nom: str
    occurrences: int = field(default=0, init=False)

    def compter(self):
        self.occurrences += 1

@dataclass
class Personnage(Corpus):
    attributs: list
    genre: str | None = None


    def identifier(self): return "personnage"
    def afficher(self): print(f"{self.nom} {self.occurrences}")

@dataclass
class Lieu(Corpus):
    categorie: str | None = None

    def identifier(self): return "lieu"
    def afficher(self): print(f"{self.nom} {self.occurrences}")

@dataclass
class Evenement(Corpus):
    date: str | None = None
    heure: str | None = None
    lieu: Lieu | None = None
    participants: list = field(default_factory=list)

    def __str__(self):
        return (f"Évenement :"
                f"nom={" ".join(self.nom.split()[:5])} ...,"
                f"date={self.date if self.date else 'N/A'},"
                f"heure={self.heure if self.heure else 'N/A'},"
                f"lieu={self.lieu.nom},"
                f"participants={
                ", ".join(p.nom for p in self.participants) if self.participants else 'N/A'
                })")

    def identifier(self): return "evenement"
    def afficher(self):
        print(f"{self.nom}, {self.date}, {self.heure}, "
              f"{self.lieu.nom if self.lieu else 'N/A'}, "
              f"{', '.join(p.nom for p in self.participants)}")