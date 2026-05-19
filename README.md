# Extracteur d'Ontologie de Narration (version 0.1)


## UTILISATION

- indiquer si installation de spacy souhaitée
- télécharger fichier depuis Projet Gutenberg en Plain Text
- indiquer chemin et nom du fichier texte à importer


## Fonctionnalités du programme

- lire un texte importé
- reconnaître les éléments ontologiques présents dans le texte selon leur catégorie (Personnage, Lieu, Événement)
- reconnaître les attributs éventuels pour chaque élément
- exporter proprement ces éléments et leurs attributs respectifs dans un fichier .csv


## Création du programme

- Ce programme a été réalisé dans le cadre du cours Programmation orientée objet : Python (SP26)
- Il est le fruit d'une collaboration de cinq étudiants, Clémence Detroyat, Gianni Caporizzo, Nathan Kunz, Guilherme Meireles Pereira et Timoté Sarrasin

## Diagrammes UML de classe et de séquence

'''mermaid
classDiagram
    class Corpus {
        +str nom
        +int occurrences
        +compter() void
    }

    class Personnage {
        +list[str] attributs
        +str|None genre
    }

    class Lieu {
        +str|None categorie
    }

    class Evenement {
        +str|None date
        +str|None heure
        +Lieu|None lieu
        +list[Personnage] participants
        +__str__() str
    }

    Corpus <|-- Personnage
    Corpus <|-- Lieu
    Corpus <|-- Evenement
    Evenement --> Lieu : lieu
    Evenement --> Personnage : participants

    class Texte {
        -_titre: str
        -_auteur: str
        -_annee: str
        +contenu: str
        +__str__() str
        +titre() str
        +auteur() str
        +annee() str
    }

    class ChargeurTexte {
        +charger(source: str) Texte
    }

    ChargeurTexte --> Texte : creates

    class AnalyseTexte {
        -personnages: list[Personnage]
        -lieux: list[Lieu]
        -evenements: list[Evenement]
        -_liste_noms_perso: list[str]
        -_liste_noms_lieux: list[str]
        +analyser(doc: Doc, min_occ: int) void
        -_ajouter_personnage(nom: str, doc: Doc) void
        -_ajouter_lieu(nom: str) void
        -_ajouter_events(doc: Doc) void
    }

    AnalyseTexte --> Personnage : creates
    AnalyseTexte --> Lieu : creates
    AnalyseTexte --> Evenement : creates

    class Exportateur {
        +ExporterPersonnages() void
        +ExporterLieux() void
        +ExporterEvenements() void
    }

    class Pipeline {
        -source: str
        -_chargeur: ChargeurTexte
        -_finder: AnalyseTexte
        -_exportateur: Exportateur
        +executer() void
    }

    Pipeline --> ChargeurTexte
    Pipeline --> AnalyseTexte
    Pipeline --> Exportateur

    class Utils {
        +spacy_conv(texte: Texte) Doc
        +nettoyer(txt: str) str
        +patienter() void
    }

    class InstallateurSpacy {
        +install_spacy() void
    }

    class fonction_perso {
        +trouver_attributs(nom: str, doc: Doc) list
        +trouver_genre(nom: str, doc: Doc) str|None
    }

    class fonctions_evenement {
        +trouver_date(texte: str) str|None
        +trouver_heure(texte: str) str|None
        +trouver_lieu(texte: str, liste_lieux: list[Lieu]) Lieu|None
        +trouver_participants(texte: str, liste_perso: list[Personnage]) list[Personnage]
    }

    AnalyseTexte ..> fonction_perso : uses
    AnalyseTexte ..> fonctions_evenement : uses
    Pipeline ..> Utils : uses
    Utils ..> InstallateurSpacy : depends on
    
![Diagramme de séquence](./docs/diagramme_timeline_UML_V2.png)
