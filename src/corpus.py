from dataclasses import dataclass, field

@dataclass
class Corpus:
    nom: str
    occurences: int = 0

    def compter(self):
        self.occurences += 1

@dataclass
class Personnage(Corpus):
    genre: str | None = None

    def identifier(self): return "personnage"
    def afficher(self): print(f"{self.nom} {self.occurences}")

@dataclass
class Lieu(Corpus):
    categorie: str | None = None

    def identifier(self): return "lieu"
    def afficher(self): print(f"{self.nom} {self.occurences}")

@dataclass
class Evenement(Corpus):
    date: str | None = None
    heure: str | None = None
    lieu: Lieu | None = None
    personnages: list = field(default_factory=list)

    def identifier(self): return "evenement"
    def afficher(self):
        print(f"{self.nom}, {self.date}, {self.heure}, "
              f"{self.lieu.nom if self.lieu else 'N/A'}, "
              f"{', '.join(p.nom for p in self.personnages)}")