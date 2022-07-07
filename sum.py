
# d={"a":[3,4,8] ,"b":[9,3,2]}
# count=0
# sum=0
# for i in d:
#     for j in (d[i]):
#         count=count+1
#         sum=sum+count
# print(sum)

# d={"a":[3,4,8],"b":[9,3,2]}
# for i in d:
#     x=d[i]
#     j=0
#     sum=0
#     while j<len(x):
#         sum+=x[j]
#         j+=1
#     d[i]=sum
# print(d)


d={"a":[3,4,8],"b":[9,3,2]}
for i in d:
    x=d[i]
    j=-1
    b=[]
    while j>=-len(x):
        b.append(x[j])
        j=j-1
        d[i]=b
print(d)
