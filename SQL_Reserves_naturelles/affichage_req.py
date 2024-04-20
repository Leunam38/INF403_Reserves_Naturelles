#!/usr/bin/python3

def affichage_requete(rep):
    if (len(rep)==0):
        print("Aucune donnée séléctionner")
        return 
    
    taille_argu=len(rep[0])
    taille_rep=len(rep)
    for i in range (taille_rep):
        print(rep[i][0], end = ' ')
        for j in range (1,taille_argu):
            print(f",{rep[i][j]}", end = ' ')
        print("")
            