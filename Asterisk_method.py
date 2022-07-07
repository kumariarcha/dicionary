# t = ('Rahul Kumar', 24, 'Agra', 'UP', 'India')
# name, age, city, *other = t
# print('Name :', name)
# print('Age :', age)
# print('City :', city)
# print('Other :', other)





from collections import Counter
dict = {'T': 23, 'U': 22, 'T': 21,'O': 20, 'R': 32, 'S': 99}
# k = Counter(my_dict)
# high = k.most_common(3)
# print("Dictionary with 3 highest values:")
# print("Keys : Values")
# for i in high:
#    print(i[0]," : ",i[1]," ")
b=[]
for i in dict:
    if dict[i]>21:
        a=dict[i]
        b.append(a)
print(b)
