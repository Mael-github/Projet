from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def dicho(FP,list):
    zga = -5
    zgb = 0
    epsilon = 0.0001
    zgmactuel = 0
    while True:
        acienzgm = zgmactuel
        zgmactuel = 0.5 * (zga+zgb)
        resultat,list = CalculPousseeArchimede(list,zgmactuel - acienzgm)
        phi = resultat - FP
        if abs(phi) < epsilon:
            return zga
        elif phi >= 0:
            zga = zgmactuel
        else:
            zgb = zgmactuel

#Produit Vectoriel en dimension 3
def ProduitVectoriel3(A,B):
    X = A[1]*B[2]-A[2]*B[1]
    Y = A[2]*B[0]-A[0]*B[2]
    Z = A[0]*B[1]-A[1]*B[0]
    Resultat = []
    Resultat.append(X)
    Resultat.append(Y)
    Resultat.append(Z)
    return Resultat

#Calcul du vecteur Ds
def CalculDS(AB,AC):
    Dsfois2 = ProduitVectoriel3(AB,AC)
    X = Dsfois2[0]/2
    Y = Dsfois2[1]/2
    Z = Dsfois2[2]/2
    Ds=[]
    Ds.append(X)
    Ds.append(Y)
    Ds.append(Z)
    return Ds

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

#Fonction pour trouver a partir des deux points le point sur la droite qui a Z = 0
def PointAuNiveauDeLeauSurLaDroite(A,B):
    AB = [B[0]-A[0],B[1]-A[1],B[2]-A[2]]
    t = float(-A[2]/AB[2])
    PointEnZ0 = [A[0]+AB[0]*t, A[1]+AB[1]*t, A[2]+AB[2]*t]
    return PointEnZ0

def TranslationSelonZ (choixtransla,list):
    for i in list:
        for y in i:
            y[2] = y[2] + choixtransla

def CalculPousseeArchimede(list,Translation):
    PousseArchimede = [0,0,0]
    #On effectue un translation de X m
    TranslationSelonZ(Translation,list)
    for i in list:
        if i[0][2] < 0 and i[1][2] < 0 and i[2][2] < 0 :
            x=CalculF(i)
            for n in range(len(PousseArchimede)) :
                PousseArchimede[n] = PousseArchimede[n] + x[n]
        elif i[0][2] < 0 or i[1][2] < 0 or i[2][2] < 0 : #cas particuliers
    #Si A est sous l'eau a chaque fois
            if i[0][2] < 0 and i[1][2] >= 0 and i[2][2] >= 0 :
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                ACen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                NouvelleCoordonnee = [i[0],ABen0,ACen0]
                x = CalculF(NouvelleCoordonnee)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n]
            elif  i[0][2] < 0 and i[1][2] < 0 :
                ACen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                PremierDecoupage = [i[0],i[1],BCen0]
                DeuxiemeDecoupage = [i[0],ACen0,BCen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
            elif i[0][2] < 0 and i[2][2] < 0 :
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                PremierDecoupage = [i[0],i[2],BCen0]
                DeuxiemeDecoupage = [i[0],ABen0,BCen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
    #Si B est sous l'eau à chaque fois
            if i[1][2] < 0 and i[0][2] >= 0 and i[2][2] >= 0 :
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                NouvelleCoordonnee = [i[1],ABen0,BCen0]
                x = CalculF(NouvelleCoordonnee)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n]
            elif  i[1][2] < 0 and i[0][2] < 0 :
                ACen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                PremierDecoupage = [i[0],i[1],ACen0]
                DeuxiemeDecoupage = [i[0],ACen0,BCen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
            elif i[1][2] < 0 and i[2][2] < 0 :
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                ACen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                PremierDecoupage = [i[1],i[2],ACen0]
                DeuxiemeDecoupage = [i[1],ACen0,ABen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
    #Si C est sous l'eau à chaque fois
            if i[2][2] < 0 and i[1][2] >= 0 and i[0][2] >= 0 :
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                CAen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                NouvelleCoordonnee = [i[2],BCen0,CAen0]
                x = CalculF(NouvelleCoordonnee)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n]
            elif  i[2][2] < 0 and i[1][2] < 0 :
                ACen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[2])
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                PremierDecoupage = [i[1],i[2],ABen0]
                DeuxiemeDecoupage = [i[2],ACen0,ABen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
            elif i[2][2] < 0 and i[0][2] < 0 :
                ABen0 = PointAuNiveauDeLeauSurLaDroite(i[0],i[1])
                BCen0 = PointAuNiveauDeLeauSurLaDroite(i[1],i[2])
                PremierDecoupage = [i[0],i[2],ABen0]
                DeuxiemeDecoupage = [i[2],ABen0,BCen0]
                x=CalculF(PremierDecoupage)
                y=CalculF(DeuxiemeDecoupage)
                for n in range(len(PousseArchimede)) :
                    PousseArchimede[n] = PousseArchimede[n] + x[n] + y[n]
    return PousseArchimede[2],list

your_mesh = mesh.Mesh.from_file('Rectangular_HULL.stl')
list = your_mesh.vectors
poidsbateau = 4.1
gravite = 9.81
FA = poidsbateau*gravite
print(dicho(FA,list))
#Si c'est actualisé
