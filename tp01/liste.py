squares = [1, 4, 9, 16, 25]

squares1 = squares
squares2 = squares[:]

print(id(squares))
print(id(squares1))
print(id(squares2))

squares[0] = 12
print(squares1)
print(squares)
print(squares2)


la_liste=[
    [0,1],
    [2,3],
    [4,5]
]
print(la_liste[1][1])
la_liste[1][1] = 12
print(la_liste)

print(50*'-')
la_liste2=la_liste[:]

print(la_liste)
print(la_liste2)
print(la_liste)
print(la_liste2)
la_liste[1][1]=24
print(la_liste)
print(la_liste2)
print(50*'-')
l1 = [0,1]
l2 = [2,3]
l3 = l2+l1

print(l3)
l3[3] = 5
print(l3)
l3.append(6)
print(l3)
s = "toto".capitalize()
print(s)
