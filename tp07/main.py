from Rectangle import Rectangle
from Carre import Carre



def showSurface(o):
    print("showSurface",o.get_surface())

def main():

    # print(Rectangle.get_cpt())
    r = Rectangle(longueur=5,largeur=6)  
    # print(Rectangle.get_cpt())
    # r1 = Rectangle(longueur=12,largeur=15)    
    # print(Rectangle.get_cpt())
    # print(r.longueur) # => 5
    # r.longueur = 12
    # print(r.longueur) # => 12
    # s = str(r)
    # print(s)

    c = Carre(2)
    c2 = Carre(2)
    # c.cote=5
    print(c.get_surface())
    
    # if c.__eq__(c2):
    if c == c2:
        print("ok")
    else:
        print("ko")


    # r = "ok" if c == c2 else "ko "

    showSurface(r)
    showSurface(c)
if __name__ == '__main__':
    main()