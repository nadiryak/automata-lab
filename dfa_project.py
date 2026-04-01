# def accepte(mot):
#     etat=0
#     for c in mot:
#         if c=='a':
#             etat=1  
#     return (etat==1 )        

# print(accepte('hibbbb')) ----> False
# print(accepte('hibbbab')) ----> True
# print(accepte('ahibbbb')) ----> True
# print(accepte('hibbbba')) ----> True
# print(accepte('')) ----> False

# implementation d'un automate (vrai modèle pour les mots qui contiennent au moins un a )
# ______________________
# ______________________
# ______________________

# En gros dans transitions on mets chaque etat avec la transition qui lui change de valeur genre key implique l'etat va avoir la valeur value  la structure d'un dictionnaire dict{key:value}

transitions={
    0:{'a':1, 'b':0},   
    1:{'a':1, 'b':1}
}
etat_intial=0

'''Dans notre cas l'etat initial c zero et pour l'etat final ou les etats finaux on met dans notre cas 1
 et ça peut avoir d'autre valeur en fnction de l'automate qu'on veut implémenter'''

etats_finaux={1} 

def accepte(mot):
    etat=etat_intial
    for c in mot :
        etat=transitions[etat][c]
    return etat in etats_finaux


# print(accepte(''))----> False
# print(accepte('hibbbb')) ---> key error, il nous dit que 'h' n'est pas définie comme clé donc il n'a pas de valeur (notre alphabet = {a,b})
# print(accepte('abbbb')) -----> True 


# _________________________________________________________________________
# _________________________________________________________________________
# _________________________________________________________________________

# on passe a implementer un automate qui contient 'ab' qui se succèdent avec un alphabet {a,b}   

transitions_2={
    0:{'a':1, 'b':0},   
    1:{'a':1, 'b':2}
}
# on garde le meme etat initial d'avant "etat_initial=0"
# par contre etats_finaux doit changer prcq dans notre cas l'etat final doit etre le fait qu'on a ab dans notre mot
etats_finaux_2={2}
def accepte_2(mot):
    etat=etat_intial
    for c in mot:
        etat=transitions[etat][c]
    return etat in etats_finaux_2    


# Maintenant on a créé une class DFA a qui on peut associer n'importe liste de tranistions etat_iniitial et etats_finaux 
# et en utilisant la fonction accepte define à l'interieur de la classe ça renvoie True si l'automate est accepté et False sinon

class DFA:


    def __init__(self, etat_initial:int, transitions:dict,etats_finaux:set ):
        self.etat_initial=etat_initial
        self.transitions=transitions
        self.etats_finaux=etats_finaux
        
    def accepte(self,mot:str):
        etat=self.etat_initial
        for c in mot:
            if c not in self.transitions[etat]:
                return f"ERROR: ton mot ne respecte pas notre alphabet"
            etat=self.transitions[etat][c]
        return etat in self.etats_finaux
dfa=DFA(0,transitions,etats_finaux)
# print (dfa.accepte("bbb"))------> False
print ((dfa.accepte("abbb")) and  (dfa.accepte("bbab")) and  (dfa.accepte("bbba")))


    




