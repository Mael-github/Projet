from Ds import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

#Calcul de la force de pression sur une facette imergée
def CalculF(Coordonee):
    p = 1.025
    g = 9.80665
    AB = [Coordonee[1][0]-Coordonee[0][0], Coordonee[1][1]-Coordonee[0][1], Coordonee[1][2]-Coordonee[0][2]]
    AC = [Coordonee[2][0]-Coordonee[0][0], Coordonee[2][1]-Coordonee[0][1], Coordonee[2][2]-Coordonee[0][2]]
    Z = float((Coordonee[0][2]+Coordonee[1][2]+Coordonee[2][2])/3)
    F = CalculDS(AB,AC)
    X = p*g*Z
    for i in range (len(F)):
        F[i] *=X
    return F

your_mesh = mesh.Mesh.from_file('Rectangular_HULL.stl')
list = your_mesh.vectors
PousseArchimede = [0,0,0]
for i in list :
    for n in range (len(PousseArchimede)):
        PousseArchimede[n] += CalculF(i)[n]
print(PousseArchimede)
