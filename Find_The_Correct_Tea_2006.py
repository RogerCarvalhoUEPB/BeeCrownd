correct_tea = str(input())
tea_list = str(input())
count =  0
for i in range (len(tea_list)):
    if tea_list[i]== correct_tea:
        count+=1
print(count)
