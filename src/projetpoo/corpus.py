from abc import ABC, abstractmethod

class Corpus(ABC):
    def __init__(self, nom: str):
        self.nom = nom
        self.occurences = 0

    def compter(self):
        self.occurences += 1

    @abstractmethod
    def identifier(self):
        pass

class Personnage(Corpus):
    # possibilité d'attribuer un age et un genre à un personnage
    def __init__(self, nom, age: int = None, genre: str = None): 
        super().__init__(nom) # récupère l'attribut de la classe parent
        self.age = age
        self.genre = genre

    def identifier(self):
        return "personnage"
    
class Lieu(Corpus):
    def __init__(self, nom, categorie: str = None):
        super().__init__(nom)
        self.categorie = categorie
        
    def identifier(self):
        return "lieu"
