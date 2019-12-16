from __future__ import print_function

from ortools.sat.python import cp_model

import random

##COMMMENTAIRE

# Le Tp a était réalisé avec le solveur cp_model
#cp_model provient de la librairie OR-Tools
#Un essai de codage a été réalisé avec pywrapcp mais ne fonctionne pas pour toutes les grilles de sodoku
#Afin d'avoir un programme final fonctionnel le solveur cp_model à donc été préféré
#Le Code qui suis regroupe 3 fonctions permettant ensemble de créer et résoudre une grille de sudoku
#A la fin de ce code est mis en commentaire le code du solveur pywrapcp
##


def GrilleAleatoire(nbcase): 
# Génère une grille de 0 de taille 9*9 avec une un certain nombre de case dont la valeur est entre 1 et 9. Le nombre de case rempli est choisi par l'utilisateur
    ligne = list(range(0, 9))
    GrilleInitiale = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 6, 0, 0, 0, 0, 0, 0, 0]]
    k=0
    while k<nbcase:
        x=random.randint(0,8)
        y=random.randint(0,8)
        if GrilleInitiale[x][y]==0:
            GrilleInitiale[x][y]=random.randint(1,9)
            k=k+1
    return(GrilleInitiale)




def Sudoku(GrilleInitiale): 
# Programme qui résoud le soduku de la grille passé en argument ( si la grille est résoluble )
    model = cp_model.CpModel()
    cellule_size = 3
    ligne_size = 9
    ligne = list(range(0, ligne_size))
    cellule = list(range(0, cellule_size))

    grille = {}
    for i in ligne:
        for j in ligne:
            grille[(i, j)] = model.NewIntVar(1, ligne_size, 'grille %i %i' % (i, j))

    # Toute les lignes différentes
    for i in ligne:
        model.AddAllDifferent([grille[(i, j)] for j in ligne])

    # Toute les colonnes différentes
    for j in ligne:
        model.AddAllDifferent([grille[(i, j)] for i in ligne])

     # Tout les "petits carrés" différents.
    for i in cellule:
        for j in cellule:
            one_cellule = []
            for di in cellule:
                for dj in cellule:
                    one_cellule.append(grille[(i * cellule_size + di,
                                          j * cellule_size + dj)])

            model.AddAllDifferent(one_cellule)

    # Initialisation des valeurs initiales.
    for i in ligne:
        for j in ligne:
            if GrilleInitiale[i][j]:
                model.Add(grille[(i, j)] == GrilleInitiale[i][j])

    # Résolution et affichage.
    resultat=0
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:
        resultat=1
        print("Grille de depart :")
        for i in ligne:
            print(GrilleInitiale[i])
        print("")
        print("Grille Résolue:")
        for i in ligne:
            print([int(solver.Value(grille[(i, j)])) for j in ligne])
    return resultat

    
    
def GenereGrille(nbcase):
    # Programme qui génère une grille de Sudoku et sa solution
    resultat=0
    while resultat==0:
        resultat=Sudoku(GrilleAleatoire(nbcase))
        


GenereGrille(17) # Appel de la fonction GenereGrillle.
# Cette appel va générer une grille de Soduku avec 17 cases préremplies et va ensuite l'afficher et afficher sa solution.






        