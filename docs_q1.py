# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# e={}
# for i in d1 :
#     if i not in d2 :
#         e[i]=d1[i]
#     else :
#         e[i]=(d1[i]+d2[i])
#     for x in d2 :
#         if x not in e :
#             e[x]=d2[x]
# print(e)


# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)



n=int(input("Input a number "))
d = dict()

for i in range(1,n+1):
    d[i]=i*i

print(d) 
