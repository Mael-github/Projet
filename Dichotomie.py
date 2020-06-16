def Dichotomie():
    ForcePoids = 21435434524543252 #constant
    PousseeArchimede = 234392489 #variable
    epsilon = 3
    PositionDuBateau = 0
    PositionPrecedente = 0
    while abs(PositionDuBateau - PositionPrecedente) > epsilon :
        PositionPrecedente = PositionDuBateau
        if PousseeArchimede > ForcePoids :
            PositionDuBateau += 0,1 #ca doit pas etre comme ca mais c'est pour l'exemple
        else :
            PositionDuBateau -= 0,1 #pareil

    return PositionDuBateau
