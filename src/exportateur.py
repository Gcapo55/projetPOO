import csv
from pathlib import Path

Hamlet = ["Hamlet","Shakespeare"]
Hamlet_personnages = ["Hamlet","Horatio","Ophelia","Claudius","Fantôme"]

count= 0

class Exportateur:

    with Path.open("test.csv", "w", newline="") as csvfile:

        fieldnames = ["Personnages"]

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()

        for personnages in Hamlet_personnages:
            count+=1
            thewriter.writerow({"Personnages":personnages})
