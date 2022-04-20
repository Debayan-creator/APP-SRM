input_list=[1,3,3,2,4,4]
l1=[]
count=0
for item in input_list:
    if item not in l1:
        count+=1
        l1.append(item)
print("No of unique items are:",count)