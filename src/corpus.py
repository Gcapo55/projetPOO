from abc import ABC, abstractmethod

class Corpus(ABC):
    """ Classe abstraite Corpus avec le nom de l'objet et un compteur d'occurences. """
    def __init__(self, nom: str):
        self.nom = nom
        self.occurences = 0

    def compter(self):
        self.occurences += 1

    @abstractmethod
    def identifier(self) -> str:
        pass

    @abstractmethod
    def afficher(self) -> str:
        pass

class Personnage(Corpus):
    """ Classe Personnage avec attribut de genre facultatif. """
    def __init__(self, nom, genre: str = None): 
        super().__init__(nom)
        self.genre = genre

    def identifier(self):
        return "personnage"
    
    def afficher(self):
        print(f" {self.nom} {self.occurences}")
    
class Lieu(Corpus):
    """ Classe Lieu avec attributs categorie facultatif. """
    def __init__(self, nom, categorie: str = None):
        super().__init__(nom)
        self.categorie = categorie

    def identifier(self):
        return "lieu"
    
    def afficher(self):
        print(f" {self.nom} {self.occurences}")
