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

#test
A = [1, 2, 0]
B = [3, 1, 2]
C = CalculDS(A,B)
print(C)
