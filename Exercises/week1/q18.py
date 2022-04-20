strmap={}
s=input("Enter the test string")
for i in s:
    if i in strmap:
        strmap[i]+=1
    else:
        strmap[i]=1
print(strmap)