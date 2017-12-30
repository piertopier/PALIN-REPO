#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:55:27 2017

@author: jean-pierrehuchet
"""
print("Palindromion - the ultimate palindrom checker")
## petit script de detection de palindrome
##
##
def sansblanc(chaine):
## Enleve les blancs et ponctuations d'une chaine de caracteres
    chainclean=[]
    for i in range(len(chaine)):
        if chaine[i] in [" ",".",",",";","!",":","?","'"]:
            continue
        else:
            chainclean.append(chaine[i])
##  print(chainclean)
    return(chainclean)
##
## Corps du programme
##
## playagain = "o"
## while playagain == "o" :
candid=input("Entre une chaine de caracteres :")
candidate = sansblanc(candid)
lg=len(candidate)
lg2=int(lg/2)

for i in range(lg2+1) :
##   print (candidate[i])
    if candidate[i]== candidate[lg-1-i]:
        palOK=("Ceci est un palindrome")
        continue
    else:
        palOK = ( "Ceci n'est pas un palindrome")
        break
print(palOK)
## playagain=input("on continue? (o/n)")
##
##
print("C'est fini !")
