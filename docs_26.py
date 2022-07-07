# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(*list(my_dict.keys()))
# a=(list(my_dict.values()))
# for i in range(len(a)):
#     print(*(a[i]))




# dict={"a":["ram"],"b":["shyam"],"c":["sita"]}
# a=dict.values()
# print(a)


# dict={"ram":["age"],"shyam":["age1"],"sita":["age2"]}
# a=dict.keys()
# print(a)



# dict={"ram":["age"],"shyam":["age1"],"sita":["age2"]}
# a=dict.keys()
# print(a)





# dict={1:1,2:4,3:6,4:16,5:25}
# dict.clear()
# print(dict)


# dict={
#     "name":"archana",
#     "class":"BA",
#     "sub":"python"
# }
# print(dict["name"])


# dict={
#     "name":"archana",
#     "class":"BA",
#     "sub":"python"
# }
# dict.popitem()
# print(dict)


# dict={1:1,2:4,3:9,4:16,5:25,6:30,7:49}
# a=dict.keys()
# print(a)



d = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
p =0
for items in d:
    if items['success'] == True:
        p+= 1
print(p)