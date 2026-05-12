import csv
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

print(values_lists)
print(fields)

filename="personnages.csv"
with open(filename, "w") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(values_lists)
