# dict={1:10,2:20,3:30,4:40,5:50,6:60}
# n=int(input("enter the num:-"))
# if n in dict:
#     print("key is present in dict")
# else:
#     print("key is not present in dict")




my_dict = {'Name': 'Sam', 'Age': 26, 'City': 'Toronto', 'Degree': 'Masters'}
print(my_dict.items())
print('Dictionary Key-Value pairs are:')
for i in my_dict.items():
    print(i)