seq=[]

n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   elm = int(input())
   seq.append(elm) 
result = filter(lambda x: x>=18, seq)
print(list(result))