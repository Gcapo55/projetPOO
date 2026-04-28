import spacy
from lecteur import AnalyseTexte

if __name__ == "__main__":
    nlp = spacy.load("fr_core_news_lg")
    nlp.add_pipe("sentencizer", before="parser")

    texte = """
    Le 3 mai à 14h30, Napoléon quitta Paris.
    A midi, la fête commença à Lyon, mais Jacob et Michel n'étaient pas là."
    Le 21 janvier 1793 à 10:00, Louis XVI fut exécuté à Paris avec Bertrand et Sophie.
    """

    doc = nlp(texte)

    analyse = AnalyseTexte(doc)
    analyse.analyser()

    print("Personnages")
    for p in analyse.personnages.values():
        p.afficher()

    print("Lieux")
    for l in analyse.lieux.values():
        l.afficher()

    print("Événements")
    for e in analyse.evenements.values():
        e.afficher()