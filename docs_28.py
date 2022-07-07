# dict=[1,2,3,4]
# a={}
# b={}
# for i in dict[::-1]:
#     a[i]=b
#     b=a
#     a={}
# print(b)




# d= {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in d:
#     d[i]=sorted(d[i])
# print(d)





student_list = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

for key,values in list(student_list.items()):
    word = ""
    for i in key:
        if i!= " ":
            word +=i
# print(word)
student_list[word] = student_list.pop(key)

print(student_list)