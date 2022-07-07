# fruit={}

# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone("Apple")
# addone("banana")
# addone("apple")
# addone("Apple")
# print(len(fruit))
# print(fruit)


# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# b={}
# for i in dic1:
#     for j in dic2:
#         for k in dic3:
#             if i==j:
#                 m=(dic1[i]+dic2[j])
# b.update({1:10})
# b.update({2:20})
# b.update({3:30})
# b.update({5:50})




my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print(*list(my_dict.keys()))
a=(list(my_dict.values()))
for i in range(len(a)):
    print(*(a[i]))