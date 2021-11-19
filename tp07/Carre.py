from Rectangle import Rectangle


class Carre(Rectangle):

    def __init__(self, cote) -> None:
        super().__init__(cote, cote)
        print("def __init__(self, cote)")
        self._cote = cote
    
    @property
    def cote(self):
            return self._cote

    @cote.setter
    def cote(self,cote):
        self.largeur = cote
        self.longueur = cote
        self._cote= cote

    def __eq__(self, o: object) -> bool:
        return o.cote == self.cote

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._cote=}"