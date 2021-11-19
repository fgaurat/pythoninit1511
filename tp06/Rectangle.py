

class Rectangle:

    _cpt=0

    def __init__(self,longueur,largeur) -> None:
        print("def __init__(self,longueur,largeur)")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    
    def get_longueur(self):
        return self._longueur

    def set_longueur(self,longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur


    def get_cpt():
        return Rectangle._cpt

    def __del__(self):
        print("def __del__(self)")