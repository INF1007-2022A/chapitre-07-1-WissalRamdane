#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
Collections import  counter


# TODO: Définissez vos fonction ici
#QUESTION 1 :
def masse_volumique_et_volume(a=1,b=2,c=3,m=4):

    volume=4/3*math.pi*a*b*c
    masse_volumique=m/volume
    print(masse_volumique)
    print(volume)
return masse_volumique ,volume

#QUSTION 2:
Phrase=input('Veuillez saisir une phrase:')
dictionnaire=counter(Phrase)
print(dictionnaire)
new_dic=(sorted(dictionnaire.items(),key=lambda item:item[0],reverse=False))
print(new_dic)

cle = max(dictionnaire, key= lambda x: dictionnaire[x])
print(new_val)

valeur_cle = max((max(dictionnaire[key]) for key in dictionnaire)

print(cle,valeur_cle)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
