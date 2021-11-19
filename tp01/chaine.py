



s1 = "L'orage gronde au loin"
s2 = 'L\'orage gronde au loin'
s3 = """
    La ligne 1
    La ligne 2
    La ligne 3
"""

s4 = '''
    La ligne 1
    La ligne 2
    La ligne 3
'''
s5 = "toto"
s6 = "tutu"
s7 = s5+s6

age = 45

age2 = '45'
int(age2)
print(type(age))
print(type(s1))
str_age = "age : "+str(45)
str_age2 = "age : "+age2
print(str_age)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5+s6)
print(50*'-')
path = r"c:\toto\nono"
print(path)

h = "Hello"
print(h[0])
print(len(h))
print(h[len(h)-1])
print(h[-1])
print(h[-2])
print(h[2:4])

print(h[:4])
print(h[2:])
print(h[:])
print(id(h))
# h[0] = 'J'
#print(h)
h = "tutu" 
print(id(h))

a= "toto"
print(id(a))
b = "toto"
print(id(b))
