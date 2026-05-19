import csv
<<<<<<< Updated upstream
#from Lecteur import AnalyseTexte

#class Exportateur:
names=["Hamlet","Horatio","Ophelia"]
values=["Hamlet","danemark","prince","Horatio","coucou","","Ophelia"]
values_lists=[]
fields=[]

for i in range(len(values)):
    if values[i] in names:
        fields.append(values[i])
        counter=0
    else:
        if counter in range(len(values_lists)):
            values_lists[counter].append(values[i])
        else:
            list=[]
            list.append(values[i])
            values_lists.append(list)
        counter+=1
=======
from corpus import Personnage,Lieu,Evenement
from Lecteur import AnalyseTexte
#from pathlib import Path
>>>>>>> Stashed changes

print(values_lists)
print(fields)

<<<<<<< Updated upstream
filename="personnages.csv"
with open(filename, "w") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(values_lists)
=======
    def __init__(self,lecteur:AnalyseTexte):

        self.personnages=list[Personnage]
        self.lieux = list[Lieu]
        self.evenements = list[Evenement]

        self.valeurs_persos=lecteur.personnages
        self.valeurs_lieux=lecteur.lieux
        self.valeurs_evenements=lecteur.evenements

    #names=["Hamlet","Horatio","Ophelia"]
    #values=["Hamlet","danemark","prince","Horatio","coucou","","Ophelia"]


    def ExporterPersonnages(self):

        values_lists=[]
        fields=[]

        for i in range(len(self.valeurs_persos)):
            if self.valeurs_persos[i] in self.personnages:
                fields.append(self.valeurs_persos[i])
                counter=0
            else:
                if counter in range(len(values_lists)):
                    values_lists[counter].append(self.valeurs_persos[i])
                else:
                    list=[]
                    list.append(self.valeurs_persos[i])
                    values_lists.append(list)
                counter+=1

        filename="personnages.csv"
        with open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(values_lists)

    def ExporterLieux(self):

        values_lists=[]
        fields=[]

        for i in range(len(self.valeurs_lieux)):
            if self.valeurs_lieux[i] in self.lieux:
                fields.append(self.valeurs_lieux[i])
                counter=0
            else:
                if counter in range(len(values_lists)):
                    values_lists[counter].append(self.valeurs_lieux[i])
                else:
                    list=[]
                    list.append(self.valeurs_lieux[i])
                    values_lists.append(list)
                counter+=1

        filename="lieux.csv"
        with open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(values_lists)

    def ExporterEvenements(self):

        values_lists=[]
        fields=[]

        for i in range(len(self.valeurs_evenements)):
            if self.valeurs_evenements[i] in self.evenements:
                fields.append(self.valeurs_evenements[i])
                counter=0
            else:
                if counter in range(len(values_lists)):
                    values_lists[counter].append(self.valeurs_evenements[i])
                else:
                    list=[]
                    list.append(self.valeurs_evenements[i])
                    values_lists.append(list)
                counter+=1

        filename="evenements.csv"
        with open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(values_lists)



>>>>>>> Stashed changes
