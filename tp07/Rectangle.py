

class Rectangle:

    _cpt=0

    def __init__(self,longueur,largeur) -> None:
        print("def __init__(self,longueur,largeur)")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur


    def get_cpt():
        return Rectangle._cpt

    def __del__(self):
        print("def __del__(self)")
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self._longueur=}, {self._largeur=}"