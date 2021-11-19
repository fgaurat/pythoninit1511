


from Rectangle import Rectangle


def main():

    # print(Rectangle.get_cpt())
    r = Rectangle(longueur=5,largeur=6)  
    del r  
    # print(Rectangle.get_cpt())
    # r1 = Rectangle(longueur=12,largeur=15)    
    # print(Rectangle.get_cpt())
    print(r.get_longueur()) # => 5
    r.longueur = 12
    print(r.longueur)
    
  


if __name__ == '__main__':
    main()