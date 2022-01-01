 # on definit la classe (vecteur 2d)
class Vecteur2D:
    x=0
    y=0
# le constructeur par defaut
# les données si les parametres ne sont pas passés
    def __init__(self,arg1=0,arg2=0): 
        self.x=arg1
        self.y=arg2

# on va tester la classe avec des objet X, Y
X=Vecteur2D() 
Y=Vecteur2D(66.0,-2)
# un vecteur nul
print(" les coordonnees cartesinnes sont : ( ",X.x," ; ",X.y," )")

#un vecteur 2D dans le plan
print(" les coordonnees cartesinnes sont : ( ",Y.x," ; ",Y.y," )")

    