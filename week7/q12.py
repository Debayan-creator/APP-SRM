from functools import reduce
scores=[]
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   elm = int(input())
   scores.append(elm) 
total = reduce(lambda a, b: a + b, scores)
print(total,max(scores))