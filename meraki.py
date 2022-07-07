# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population)


# Dict = {
#     'ball' : 'green',
#     'Ball': 'red',
# }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])




# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation',
# }

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)







# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{'organisation':'navgurukul','place':'dharamsala',}

# }
# print(person['gender'])
# print(person[4])
# result=person[4]["place"]
# print(result)



# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
# }
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)




# dict={
#     "name":"archana",
#     "student":"rohini",
#     "class":12,
# }
# dict["age"]=20
# dict["town"]="kishanganj"
# print(dict)



# dic= {
#     'Name': 'RAM',
#     'Age': 17,
# }
# dic['student']={
#     'id':22, 
#     'place':'dharamsala'
# }
# print(dic)




# dict={
#     "name":"archana",
#     "class":"BA",
# }
# dict["student"]={
#     "age":18,
#     "place":"kishanganj"

# }
# print(dict)




# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
#     }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")



# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#     }
# mydict=classes.copy()
# print(mydict)



data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
c=[]
for key in data:
    for i in key:
        if key[i] in c:
            pass
        else:
            c.append(key[i])
print(c)