def Dichotomie(): #on l'utilisera pas en fonction mais plus dans une boucle while
    PoidsduBateau = 8 #demander a l'utilisateur
    Gravite = 9.80665 #demander a l'utilisateur
    ForcePoids = PoidsduBateau*Gravite
    PousseeArchimede = 234392489 #variable, on appelle la fonction en boucle
    epsilon = 3
    PositionDuBateau = 0
    PositionEnDessousMax = -500000
    PositionAuDessusMin = 500000
    while abs(PositionAuDessusMin - PositionEnDessousMax) > epsilon :
        if PousseeArchimede > ForcePoids :
            PositionDuBateau += 0,1  #ca doit pas etre comme ca mais c'est pour l'exemple
            if PositionEnDessousMax < PositionDuBateau : #Pour obtenir la position la plus proche en dessous de la position d'équilibre
                PositionEnDessousMax = PositionDuBateau
        else :
            PositionDuBateau -= 0,1 #pareil
            if PositionAuDessusMin > PositionDuBateau : #Pour obtenir la position la plus proche au dessus de la position d'équilibre
                PositionAuDessusMin = PositionDuBateau
    return PositionAuDessusMin,PositionEnDessousMax,PositionDuBateau
