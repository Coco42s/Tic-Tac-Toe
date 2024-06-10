"""
Corentin
5/12/22
code tic tac toe
notion: tableau de tableau, modulaire...
"""

# Bonjour,
# Ceci est ma vertion de mon tic_tac_toe.
# Je n'est pas pris le temp de soigné l'affichage mais il restre sobre.
# Les fonction ne sont pas d'étailler comme dans le Main. 
# Les global son présent même si vous mavez dit de les utiliser les moin posible il sont la car j'ai pas envie de compléxifier mon script alors qu'il les déjà.
# Bonne Correction.

"""

Se scripte comprend 18 Fonction et un Main de 13 ligne.

"""


##--- Import des blibliotèque ---##
from random import randint

##--- Création des fonction ---##
def Premier_Joueur(J1,J2):
    """ La fonction permet de mettre dans un tableau le nom des joueur et leur sygne et de choisire le joueur de magnière aléatoire
        J1 (_int_): Nom du joueur 1
        J2 (_int_: Nom du joueur 2
    Returns:
        res (_list_): le tableau de joueur
    """
    alea_joueur=randint(1,2)
    if alea_joueur==1:
        res=[[J1,"X"],[J2,"O"]]
    else:
        res=[[J2,"X"],[J1,"O"]]
    return(res)

def aTonTour(symb,premier_joueur):
    """Permès d'échanger le joueur et le symbole en cour d'utilisation
    Args:
        symb (_str_): _symbole en cour dutilisation_
        premier_joueur (_list_): _liste avec les joueur et les symbole_
    Return: 
        premier_joueur[1][1] et premier_joueur[0][1] = des sybole
        premier_joueur[0][0] et premier_joueur[1][0] = les nom des joueur
    """
    if symb==premier_joueur[0][1]:
        return(premier_joueur[1][1],premier_joueur[1][0])
    else: 
        return(premier_joueur[0][1],premier_joueur[0][0])


#-- Aficher --#

def affiche_pts(pts,premier_joueur):
    """Cet fonction perment d'afficher les pionts de magnier propre (a mètre dans un print)

    Args:
        pts (_list_): pts est le tableaux des points
        premier_joueur (_type_): ceci est le tableaux des joueur actuelement en place

    Returns:
        rep (_str_): suite de caractaire pairmétan d'afficher les point 
    """
    rep="\n\nLes score sont :\n   - "+premier_joueur[0][0]+" avec "+str(pts[0])+" pts\n   - "+premier_joueur[1][0]+" avec "+str(pts[1])+" pts"
    return rep

def affiche(tab):
    """Cette permet d'afficher un tableaux de magnière propre. il faux que se soit un tableua de ce type : [[_,_,_],[_,_,_],[_,_,_]]

    Args:
        tab (_list_): le tableaux voulu

    Returns:
        af (_str_): suite de caractaire pairmétan d'afficher le tableux
    """
    af="\n   "+str(tab[0][0])+" "+str(tab[0][1])+" "+str(tab[0][2])+"\n   "+str(tab[1][0])+" "+str(tab[1][1])+" "+str(tab[1][2])+"\n   "+str(tab[2][0])+" "+str(tab[2][1])+" "+str(tab[2][2])+"\n"
    return af


#-- Tableaux --#

def tab_point():
    """Cette fonction permet de généré un tableux de jeux rempli avec des points

    Returns:
        tab (_list_) : tableau de points
    """
    tab=[["." for k in range(3)]for i in range(3)]
    return tab

def tab_num():
    """Cette fonction permet de généré un tableux rempli avec des numéraux

    Returns:
        tab (_list_): tableau de numéraux
    """
    tab=[[k+1+3*i for k in range(3)]for i in range(3)]
    return tab


#-- Jouer --#

def joue(symb,num,tjeux):   
    """cette fonction permet de modifier le tableau de jeux avec le choi du joueur. Si le chois n'est pas corecte la fonction renvoi 1.

    Args:
        symb (_str_): symb de jeux actuelle
        num (_int_): chifre voulu par le joueur
        tjeux (_list_): tableaux de jeux

    Returns:
        _int_: erreur 
        _none_: pas besoit de renvoiller quelque chose 
    """
    num-=1
    if (tjeux[num//3][num%3] == "X") or (tjeux[num//3][num%3] == "O"):
        return 1
    else:    
        tjeux[num//3][num%3]=symb
    return 

def joueur_rep(num,symb,tjeux):
    """cette fonction permait de prendre les action du joueur quand il repon de ou il veux jouer.

    Args:
        num (_int_): choix du joueur
        symb (_str_): symbol en cour d'utilisation
        tjeux (_list_): tableaux du jeux

    Returns:
        rep (_str_): mauvai choi du joueur ou demende du joueur
        tjeux (_list_): tableau de jeux modifier
    """
    global j_rep,dad
    if num<10:            
        val=joue(symb,num,tjeux)          
        if type(val)==int:
            dad,rep=1,"\n\nil y a déjà un pion ici" 
            return rep
        else:                    
            j_rep=True 
            return tjeux         
    elif num==10:
        dad,rep=1,"\n\nVoici le jeu avec les numéros :"+affiche(t_num)
        return rep
    else:
        dad,rep=1,"\n\nMauvais choix"
        return rep

def Finie_vérif(tjeux,tabdiag,text,premier_joueur):
    """Cette fonction permet de vérifier si le jeux est finie, de mètre a jour les point, de changer de joueur et de sybol, et de demender si on rejoue
    
    Args:
        text (_list_): liste des text
        tjeux (_list_): le tableux du jeux
        tabdiag (_list_): point por ou passer
        premier_joueur (_list_): ceci est le tableaux des joueur actuelement en place
    
    Returns:
        _str_: soit sais un text pour dire que sais finie, soit un text avec rien
        
    Global:
         symb,joueur,jeux_finie,pts,demende_rejoue: tout sais variable son indispensable mais ne son inutile au return; demende_rejoue=pour accédé a la demende de rejoue; pts=les point en vigeur.
    """
    global symb,joueur,jeux_finie,pts,demende_rejoue
    tf,diag,colone,ligne=0,DetectDiag(symb,tjeux,tabdiag),detectColone(symb,tjeux),detectLigne(symb,tjeux)
    for i in range(0,9):
        if (tjeux[i//3][i%3] == "X") or (tjeux[i//3][i%3] == "O"):
            tf+=1    
        else:
            tf=0
    if (ligne or colone or diag) == True:  
        if symb=="X":
            pts[0]+=1
        else:
            pts[1]+=1
        text,demende_rejoue=text_rel(),True
        return text[2][0]
    elif tf == 9:
        demende_rejoue=True
        return text[2][1]
    else:
        symb,joueur=aTonTour(symb,premier_joueur)
        return ""


#-- Détéction --#

def detectLigne(symb,tjeux):
    """Cette fonction permet de férifier si une ligne est complété par les même simbole qui est définie par symb

    Args:
        symb (_str_): symbol en vigeur
        tjeux (_list_): le tableux du jeux

    Returns:
        _bool_: passe a True une ligne est finie sinon False
    """
    a=0
    for i in range(3):
        for k in range(3):
            if tjeux[i][k] == symb:
                a+=1
        if a==3:
            return True
        else:
            a=0
    return False

def detectColone(symb,tjeux):
    """Cette fonction permet de férifier si une cologne est complété par les même simbole qui est définie par symb

    Args:
        symb (_str_): symbol en vigeur
        tjeux (_list_): le tableux du jeux

    Returns:
        _bool_: passe a True une cologne est finie sinon False
    """
    a=0
    for i in range(3):
        for k in range(3):
            if tjeux[k][i] == symb:
                a+=1
        if a==3:
            return True
        else:
            a=0
    return False

def DetectDiag(symb,tjeux,tabdiag):
    """Cette fonction permet de férifier si une diagonal est complet en fonction de simbole. elle le férifien en passen par les point indiquer dans tabdiag.
    
    Args:
        symb (_str_): symbol en vigeur
        tjeux (_list_): le tableux du jeux
        tabdiag (_list_): point por ou passer

    Returns:
        _bool_: passe a True une diagonal est finie sinon False
    """
    a=0
    for i in tabdiag[0]:
        if tjeux[i//3][i%3] == symb:
            a+=1
    if a!=3:
        a=0
        for i in tabdiag[1]:
            if tjeux[i//3][i%3] == symb:
                a+=1
    if a==3:
        return True
    else:
        return False


#--  Points --#

def points_finie(premier_joueur,pj_save):
    """invercition des points si il y a une inverstion des joueur lors de relence du jeux

    Args:
        premier_joueur (_list_): Nouvelle vertion de de la liste des joueur et des signe
        pj_save (_str_): sauvegarde du nom du premier joueur

    Returns:
        nex pts (_list_): nouvelle versition des point
    """
    global pts
    if premier_joueur[0][0]!=pj_saves:
        pts1,pts2=pts[0],pts[1]
        new_pts=[pts2,pts1]
    else:
        new_pts=pts
    return new_pts


#-- Inite and reload --#

def text_rel():
    """Permet de maitre le text avec les nouvelle valeur

    Returns:
        _list_: nouveaux text
    """
    text=[["\nLe but du jeu est :\n - Le but du jeu est d'aligner avant son adversaire 3 symboles identiques horizontalement, verticalement ou en diagonale.\n\nLes règle son :\n - Le joueur énoncé commence en premier\n - Vous devez taper le numéro de la case puis sur 'entrée' pour placer votre pion\n - On ne peut mettre un pion sur une case déjà jouée\n - Si vous voulez voir le tableau avec les nombres taper : 10\n - Amusez-vous bien !\n\nLe tableau sera:"+affiche(t_num)[0]],
          ["\nLe joueur nommé "+str(premier_joueur[0][0])+" jouera en premier !\nIl lui est attribué le symbole X"],
          ["\n"+affiche(tjeux)+"\n\nBravo "+str(joueur)+" tu as gagné !"+affiche_pts(pts,premier_joueur),"\n"+affiche(tjeux)+"\n\nMatch nul perssone as gagné !"+affiche_pts(pts,premier_joueur)],
          [", le jeu est :"],
          [", où veux-tu jouer ? "],
          [symb]]
    return text

def init(J1,J2):
    """Cette fonction perment de définire plusieur variable indispansable pour le bon déroulement du jeux

    Args:
        J1 (_str_): Nom du joueur 1
        J2 (_str_): Nom du joueur 2

    Returns:
        _all_: plusieur variable indispensable au bon d'éroulement du jeux
    """
    premier_joueur=Premier_Joueur(J1,J2)
    t_num,tjeux,joueur,symb,tabdiag,jeux_finie,pts,pj_saves,demende_rejoue=tab_num(),tab_point(),premier_joueur[0][0],premier_joueur[0][1],[[8,4,0],[6,4,2]],False,[0,0],premier_joueur[0][0],False
    text=[["\nLe but du jeu est :\n - Le but du jeu est d'aligner avant son adversaire 3 symboles identiques horizontalement, verticalement ou en diagonale.\n\nLes règle son :\n - Le joueur énoncé commence en premier\n - Vous devez taper le numéro de la case puis sur 'entrée' pour placer votre pion\n - On ne peut mettre un pion sur une case déjà jouée\n - Si vous voulez voir le tableau avec les nombres taper : 10\n - Amusez-vous bien !\n\nLe tableau sera:"+affiche(t_num)[0]],
          ["\nLe joueur nommé "+str(premier_joueur[0][0])+" jouera en premier !\nIl lui est attribué le symbole X"],
          ["\n"+affiche(tjeux)+"\n\nBravo "+str(joueur)+" tu as gagné !"+affiche_pts(pts,premier_joueur),"\n"+affiche(tjeux)+"\n\nMatch nul perssone as gagné !"+affiche_pts(pts,premier_joueur)],
          [", le jeu est :"],
          [", où veux-tu jouer ? "],
          []] # je nais pas u le temps de tout mètre dans la variable text. (j'ai aussi d'otre devoir)
    print(text[0][0],"",text[1][0])
    return tjeux,t_num,symb,joueur,premier_joueur,text,tabdiag,jeux_finie,pts,pj_saves,demende_rejoue


#-- Rejoue --#

def rejouer():
    """permet de demender au joueur si ils veilent rejouer, si oui il réinitialiser sertaine valeur sinon il arr¨te le jeux avec jeux finie

    Returns:
        _str_: indication
    """
    global jeux_finie,premier_joueur,tjeux,joueur,symb,pj_saves,demende_rejoue,pts
    val_rejoue=int(input("\nVoulez-vous rejouer... (]Si oui taper 1 dans le cas contrère taper 0[) : "))
    if val_rejoue==1:
        premier_joueur,rep=melenge(premier_joueur),"\n\nLe Jeux recommence !!"
        pts=points_finie(premier_joueur,pj_saves) 
        tjeux,joueur,symb,pj_saves,demende_rejoue=init_rejoue()
          
    else:
        jeux_finie=True
        rep="\narrêt..."
    return rep

def init_rejoue():
    """permet de remètre sertaine variable a 0

    Returns:
        _all_: plusieur variable indispensable au bon d'éroulement du jeux remise a 0
    """
    global tjeux,joueur,symb,pj_saves,demende_rejoue
    tjeux,joueur,symb,pj_saves,demende_rejoue=tab_point(),premier_joueur[0][0],premier_joueur[0][1],premier_joueur[0][0],False
    return tjeux,joueur,symb,pj_saves,demende_rejoue

def melenge(premier_joueur):
    """cette fonction permet d'échenger les joueur de magnière aléatoire

    Args:
        premier_joueur (_list_): ancien premier joueur : ordre des joueur
    
    Return:
        _list_: nouveaux premier joueur 
    """
    alea_joueur,J1,J2=randint(1,2),premier_joueur[0][0],premier_joueur[1][0]
    if alea_joueur==1:
        res=[[J1,"X"],[J2,"O"]]
    else:
        res=[[J2,"X"],[J1,"O"]]
    return(res)


##--- Main ---##
tjeux,t_num,symb,joueur,premier_joueur,text,tabdiag,jeux_finie,pts,pj_saves,demende_rejoue=init(str(input("Nom du joueur 1 : ")),str(input("Nom du joueur 2 : ")))
while not jeux_finie: # Boncle de jeux
    j_rep=False
    while not j_rep: # Boncle de joueur: ne se finie pas tanque le joueur na pas répondu corèctement
        print("\n\n"+str(joueur),text[3][0]+affiche(tjeux))
        num,dad=int(input(str(joueur)+text[4][0])),0 # dad est une variable d'erreur
        erreur=joueur_rep(num,symb,tjeux)
        text=text_rel() # a se niveaux on a besoins de reload le text même si dans finie vérif il y en a d'éja 1
        if dad==1: 
            print(erreur)
    fin=Finie_vérif(tjeux,tabdiag,text,premier_joueur)
    print(fin) # ne printe rien quand le jeux n'ai pas finie
    if demende_rejoue==True: # est active a la fin du jeux
        print(rejouer())