from collections import deque

l = [12,5,9]
print(l)
l.append(25)
print(l)
i = l.pop()
print(i,l)

d = deque(l)
print(d)
d.appendleft(10)
print(d)
print(l)

a=[]

for i in range(10):
    if i%2 == 0:
        a.append(i)
print(a)

a=list(map(lambda i:i, range(10)))
print(a)


a = [i for i in range(10) if i%2 == 0]
print(a)


s = ["tutu","toto","tata"]
# s1  =>["Tutu","Toto","Tata"]

s1 = [v.capitalize() for v in s]
print(s1)

l1 = [i for i in range(5)]
l2 = [i for i in range(5,10)]
print(l1)
print(l2)
l3 = list(zip(l1,l2))

a  =[10,11,22,43]

if 10 in a:
    print("ok")

for i,v in enumerate(a):
    print(i,v)

a  =[10,11,22,43,10,22,43]
a = list(set(a))
print(a)

d = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4",
    }
print(d)

for k,v in d.items():
    print(k,v)
    # print(k,d[k])