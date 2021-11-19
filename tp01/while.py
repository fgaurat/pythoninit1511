f=[]
a, b = 0, 1
while a < 1000:
    # print(a,end=',')
    f.append(a)
    a, b = b, a+b

print(len(f))
print(f)