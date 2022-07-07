# key_value={"a":4,"b":5,"c":6,"d":10}
# m=0
# n=0
# for i in (key_value):
#     m=max(key_value)
#     n=min(key_value)
# print("max",m)
# print("min",n)





# key={"Archana":3000,"nisha":5000,"annu":600}
# a=0
# b=0
# for i in (key):
#     a=max(key)
#     b=min(key)
# print(a)
# print(b)




student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
temp=[]
res={}
for key,value in student_data.items():
    if value not in temp:
        temp.append(value)
        temp=student_data[key]=value
print(res)
