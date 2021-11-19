
def add(*l):
    print(type(l))
    print(l)
    r = 0
    for i in l:
        r+=i
    return r

data = [5,6,7,8]
s = add(*data)
s = add(5,6)
s = add(5,6,15,78,98,14)
print(s)



def hello(**data):
    print(type(data))
    print(data)
    name = data['name']
    first_name = data['first_name']
    print("Bonjour",name,first_name)

hello(name="DURAND",first_name="Robert")

d = {"name":"DURAND","first_name":"Robert"}
    
hello(**d)
print(d['name'])

for k in d:
    print(k,d[k])


def f(a:int="toto")->int:
    print(a)
    return 12

f(a="toto")
f("toto")