# a="123"
# b="12"
# c=[]
# i=0
# while i<len(a):
#     if a>b:
#         c=b+a+b
#     else:
#         c=a+b
#     i=i+1
# print(c)



def sum_of_elements(num_list,number):
    result_sum=0 
    i=0 
    while(i<len(num_list)):
        if num_list[i]==number or (i+1<len(num_list) and num_list[i+1]==number) or (i-1>=0 and num_list[i-1]==number):
            pass
        else:
            result_sum+=num_list[i]
        i+=1
    
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))