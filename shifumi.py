import random

# Liste des possibilités pour que l'ordi puisse faire un choix aléatoire
shifumi = ['p','c','f']
# On demande au joueur le nombre de fois qu'il veut jouer avec un input qui sera un nombre donc que l'on convertit en int
nb_manche_voulu = int(input("Entrez le nombre de manche que vous souhaitez ?"))
# Initialisations des variables
score_j = 0
score_ord = 0
nb_manche = 0

# La condition tant que pour jouer le nombre de manches souhaité
while nb_manche < nb_manche_voulu:
    # On demande le choix du joueur et on prend le choix de l'ordi de façon aléatoire
    choix_joueur = input("Entrez votre choix Pierre(p), Ciseaux(c) et Feuille(f) ?")
    choix_ordi = random.choice(shifumi)
    # Toutes les possibilités dans lesquelles le joueur gagne
    if (choix_joueur == 'p' and choix_ordi == 'c') or (choix_joueur == 'c' and choix_ordi == 'f') or (choix_joueur == 'f' and choix_ordi == 'p'):
        print("Joueur gagne !")
        score_j+=1
    # Toutes les possibilités dans lesquelles il y a égalité
    elif (choix_joueur == 'p' and choix_ordi == 'p') or (choix_joueur == 'c' and choix_ordi == 'c') or (choix_joueur == 'f' and choix_ordi == 'f'):
        print("Egalité !")
    # Toutes les possibilités dans lesquelles le joueur perd
    elif (choix_joueur == 'c' and choix_ordi == 'p') or (choix_joueur == 'f' and choix_ordi == 'c') or (choix_joueur == 'p' and choix_ordi == 'f'):
        print("Ordi gagne !")
        score_ord+=1
    # On incrémente le nombre de manche après en avoir joué une
    nb_manche+=1

# On compare les scores connaitre le résultat du match
if score_j>score_ord:
    print("Joueur gagne le match ! J:"+str(score_j)+" vs O:"+str(score_ord))
elif score_ord == score_j:
    print("Egalité dans ce match ! J:"+str(score_j)+" vs O:"+str(score_ord))
else:
    print("Ordi gagne le match ! J:"+str(score_j)+" vs O:"+str(score_ord))
