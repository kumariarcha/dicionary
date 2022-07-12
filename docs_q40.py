# a= ['S001', 'S002', 'S003', 'S004']
# b = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c = [85, 98, 89, 92]
# d=[]
# e=[]
# for i in range(len(b)):
#     l={}
#     for j in range(len(c)):
#         if i==j:
#             l.setdefault(b[i],c[j])
#             d.append(l)
# for k in range(len(a)):
#     l2={}
#     l2.setdefault(a[k],d[k])
#     e.append(l2)
# print(e)



dict = {"one":1, "two":2, "three":3}
print(dict.setdefault("one"))