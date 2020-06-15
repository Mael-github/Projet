from Ds import *
#Calcul de la force de pression sur une facette imergée
def CalculF(Coordonee):
    p = 1.025
    g = 9.80665
    AB = [Coordonee[1][0]-Coordonee[0][0], Coordonee[1][1]-Coordonee[0][1], Coordonee[1][2]-Coordonee[0][2]]
    AC = [Coordonee[2][0]-Coordonee[0][0], Coordonee[2][1]-Coordonee[0][1], Coordonee[2][2]-Coordonee[0][2]]
    Z = (Coordonee[0][2]+Coordonee[1][2]+Coordonee[2][2])/3
    F = p*g*Z*CalculDS(AB,AC)
    return F

