def main():
    age = 45.3333333

    s = f"l'âge est : {age}"
    s1 = "l'âge est : {0}".format(age)
    s12 = "l'âge est : {}".format(age)
    s13 = "l'âge est : {age}".format(age=age)
    s2 = f"{age=}"
    print(s)
    print(s1)
    print(s2)

    a=3
    b=2
    c = 2/3
    print(f"la valeur de c = {c:.2}")
    print(f"pourcentage de c = {c:.2%}")
    
    age = 45.3333333
    print(age,type(age))
    s3 = f"{age=:.4f}"
    s31 = f"{age=:.4}"
    print(s3)
    print(s31)

    l = ['Robert','DURAND',45]
    d = {'prenom':'Robert','nom':'DURAND','age':45}
    print("{0} {1} {2}".format(*l))
    print("{prenom} {nom} {age}".format(**d))

if __name__ == '__main__':
    main()
