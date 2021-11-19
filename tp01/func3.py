

# def mult2(l):
#     r = []
#     for v in l:
#         r.append(v*2)

#     return r
# def mult2(v):
#     return v*2


values = [1,2,3,4]
# result = mult2(values)
result2 = list(map(lambda v:v*2,values))
# print(result) # [2,4,6,8]
print(result2) # [2,4,6,8]

