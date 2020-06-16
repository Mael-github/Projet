from Ds import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

#Calcul de la force de pression sur une facette imergée
def CalculF(Coordonee):
    p = 1.025
    g = 9.80665
    #calcul des vecteurs AB et AC
    AB = [Coordonee[1][0]-Coordonee[0][0], Coordonee[1][1]-Coordonee[0][1], Coordonee[1][2]-Coordonee[0][2]]
    AC = [Coordonee[2][0]-Coordonee[0][0], Coordonee[2][1]-Coordonee[0][1], Coordonee[2][2]-Coordonee[0][2]]
    Z = float((Coordonee[0][2]+Coordonee[1][2]+Coordonee[2][2])/3)
    F = CalculDS(AB,AC)
    X = p*g*Z
    for i in range (len(F)):
        F[i] = F[i]*X
    return F

#Permet de translater le bateau selon Z
def TranslationSelonZ (choixtransla):
    for i in your_mesh.vectors:
        for y in i:
            y[2] = y[2] - choixtransla

your_mesh = mesh.Mesh.from_file('Rectangular_HULL.stl')
list = your_mesh.vectors
PousseArchimede = [0,0,0]
#On effectue un translation de 5m
TranslationSelonZ(5)
for i in list:
    if i[0][2] < 0 and i[1][2] < 0 and i[2][2] < 0 :
        x=CalculF(i)
        for n in range(len(PousseArchimede)) :
            PousseArchimede[n] = PousseArchimede[n] + x[n]
    elif i[0][2] < 0 or i[1][2] < 0 or i[2][2] < 0 :
        print("facettes à moitié immergée")
        #cas a traiter
print(PousseArchimede)


