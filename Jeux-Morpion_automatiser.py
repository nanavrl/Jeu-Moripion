
''' Projects n°1 : NSI 1G2 // Anna Viroulaud // Sujet n°6 : Trois pions ,neuf cases  '''

# ------------------------------------------

''' importation des biblioteques nécessaires au programme '''

import random                                    # Importer la biblioteque random (aleatoire)

# ------------------------------------------

''' Etre sur de placer un pion dans une case qui n'a pas deja était choisi aleatoirement '''

def tirer_des_pions():                           # Définition d'une fonction "tirer des pions"
    grille= [[0,0,0],[0,0,0],[0,0,0]]            # Crée une liste " [[0,0,0],[0,0,0],[0,0,0]]" nommée grille
    for i in range (3):                          # Pour i repeter (3 fois)
        case_choisi=False                        # Affecter Faux a la case_choisi
        while case_choisi==False:                # Tant que la case_choisi est Faux alors repeter
            ''' choisir aleatoirement la ligne et la case '''
            ligne=random.randint (0,2)           # Choisir un tableau aleatoire
            case=random.randint(0,2)             # Choisir une case aleatoire
            if grille[ligne][case]==0:           # Si case est equivalent a 0
                grille[ligne][case]=1            # Dans la grille, changer le 0 de la case dans la ligne choisi en 1²
                case_choisi=True                 # Affecter donc Vrai a la case_choisi
    return grille                                # Retourner grille

# ------------------------------------------

''' Definir la fonction coup_gagnant qui defini les combinaison gagnante '''

def combinaison_gagnante(grille):                # Définition fonction coups_gagnants

    ''' Les different combinaison gagnante sont definie ainsi que leurs pointss associés paramètres: grille ---> tableau '''

    combinaison_0=[[0,1,0],[0,1,0],[0,1,0]]      # Affecter la liste "[[0,1,0],[0,1,0],[0,1,0]]" a combinaison_0
    combinaison_1=[[1,1,1],[0,0,0],[0,0,0]]      # Affecter la liste "[[1,1,1],[0,0,0],[0,0,0]]" a combinaison_1
    combinaison_2=[[0,0,1],[0,1,0],[1,0,0]]      # Affecter la liste "[[0,0,1],[0,1,0],[1,0,0]]" a combinaison_2
    combinaison_3=[[1,0,0],[1,0,0],[1,0,0]]      # Affecter la liste "[[1,0,0],[1,0,0],[1,0,0]]" a combinaison_3
    combinaison_4=[[0,0,1],[0,0,1],[0,0,1]]      # Affecter la liste "[[0,0,1],[0,0,1],[0,0,1]]" a combinaison_4
    combinaison_5=[[0,0,0],[0,0,0],[1,1,1]]      # Affecter la liste "[[0,0,0],[0,0,0],[1,1,1]]" a combinaison_5
    combinaison_6=[[0,0,1],[0,1,0],[1,0,0]]      # Affecter la liste "[[0,0,1],[0,1,0],[1,0,0]]" a combinaison_6
    combinaison_7=[[0,0,0],[1,1,1],[0,0,0]]      # Affecter la liste "[[0,0,0],[1,1,1],[0,0,0]]" a combinaison_7

    ''' Puis definir les points en fonction des combinaisons '''

    if grille==combinaison_0 :                   # Si grille est equivalente a combinaison_0
        points= "4"                              # Affecter "4" a points
        return "horizontale : 4 points",4             # Retourner "milieu : 4 points",4

    elif grille==combinaison_7:                  # Sinon si grille est equivalente a combinaison_7
        points="4"                               # Affecter "4" a points
        return "vertical : 4 points",4             # Retourner "milieu : 4 points",4

    elif grille==combinaison_1:                  # Sinon si grille est equivalente a combinaison_1
        points="1"                               # Affecter "1" a points
        return "coté : 1 point",1                # Retourner "coté : 1 point",1

    elif grille==combinaison_3:                  # Sinon si grille est equivalente a combinaison_3
        points="1"                               # Affecter "1" a points
        return "coté : 1 point",1                # Retourner "coté : 1 point",1

    elif grille==combinaison_4:                  # Sinon si grille est equivalente a combinaison_4
        points="1"                               # Affecter "1" a points
        return "coté : 1 point",1                # Retourner "coté : 1 point",1

    elif grille==combinaison_5:                  # Sinon si grille est equivalente a combinaison_5
        points="1"                               # Affecter "1" a points
        return "coté : 1 point",1                # Retourner "coté : 1 point",1

    elif grille==combinaison_2:                  # Sinon si grille est equivalente a combinaison_2
        points="16"                              # Affecter "1" a points
        return "diagonale : 16 points",16        # Retourner "diagonale : 16 points",16

    elif grille==combinaison_6:                  # Sinon si grille est equivalente a combinaison_6
        points="16"                              # Affecter "1" a points
        return "diagonale : 16 points",16        # Retourner "diagonale : 16 points",16

    else:                                        # Sinon
        points="0"                               # Affecter "0" a points
        return "Rien",0                          # Retourner rien,0

# ------------------------------------------

''' Definir la fonction jouer_une_partie pour la reutiliser dans le programe, et definir Le joueur gagnant '''

def jouer_une_partie():                          # Définition fonction jouer_une_partie
    ''' Cette fonction permet de definir le nombre de partie ainsi que le nombre de joueur et le/les gagnant'''
    for nombre_de_partie in range (25):          # Pour nombre_de_partie repeter (le nombre de partie que vous voulez)
        le_gagnant_est =  "Pas de gagnant "      # Definir le gagnant comme pas de gagnant
        le_max_est = 0                           # Dire que le max est de 0
        egalité = "Egalité"                      # Definir une Egalité quand la console trouver egalité
        print("************** partie n°", nombre_de_partie+1,"**************") # Ecrire "*************" nombre de partie et ajouter 1 a chaque nouvelle partie "**************"
        ''' Definir le nombre de joueur '''
        for j in range (9):                      # Pour j (9 fois)
            grille = tirer_des_pions()           # Affecter tirer_des_pions() a grille
            info_points,point= (combinaison_gagnante(grille)) # Affecter la combinaison_gagnant de la grille a info_points,point
            print ("joueur",j+1, "   tirage=",grille,"-->",info_points) # Ecrire dans la console " ( Le joueur avec sont numero puis le grille tiré --> et puis les points ) "
            if  point > le_max_est:              # Traite si point et superieur a le_max_est qui est egal a 0
                le_max_est = point               # Affecter point a le_max_est
                le_gagnant_est = j+1             # dire que j+1 est le_gagnant_est
            elif (point == le_max_est and point != 0): # Sinon si point est equivalent a le_max_est et point different de 0 :
                le_gagnant_est = egalité         # Affecter egalité a le_gagnant_est
        ''' Definir se qui sera ecrit dans la console en fonctions des resultats obtenu '''
        if le_max_est != 0 and le_gagnant_est != egalité : #Traite le joueur gagnant
            print ( "Le gagnant est le joueur n°" , le_gagnant_est, "avec", le_max_est, "points.") # Ecrire dans la console le gagnant et le numero du joueur : le_gagnant_est et le maximum de point de la partie : le_max_est
        if le_max_est == 0:                      # Traite si il n 'y a pas de gagnant
            print ("Il n'y a pas de gagnant.")   # Ecrire dans la console que il n'y a pas de gagnant
        if le_gagnant_est == egalité :           # traite si il y a égalité entre les joueurs
            print ("Il y a egalité entre les joueurs , ils ont tous", le_max_est, "points.") # ecrire dans la console qu'il y a egalite et dire de combien de point et l'egaliter grace a u point max attein pendant 1 partie: le_max_est

# ------------------------------------------

''' Ecrire les premières informations dans la console '''

print ("Sujet n°6 : Trois pions ,neuf cases")    # Ecrire dans la console "Projet n°6 : Trois pions ,neuf cases"

''' Avant de commencer la partie demander au joueur si il veut jouer '''

reponse=input ("Bonjour, voulez-vous jouer ? ")  # Demander dans la console "Bonjour, voulez-vous jouer ?"
if reponse=="oui":                               # Si la reponse est equivalente a "oui"
    jouer_une_partie()                           # Apelle de la fonction jouer_une_partie
else:                                            # Sinon
    print("A bientot , N'esiter a re venir si vous voulez jouer une partie.") # Ecrire "Au revoir" dans la console






