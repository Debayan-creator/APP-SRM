nums1=[]
nums2=[]
def add_sub(x, y):
    return x + y, x - y
 
n = int(input("Enter number of elements in the listA : "))
for i in range(0, n):
   elm = int(input())
   nums1.append(elm) 

n = int(input("Enter number of elements in the listB : "))

for i in range(0, n):

   elm = int(input())
   nums2.append(elm) 

print("Original lists:")
print(nums1)
print(nums2)
result = map(add_sub, nums1, nums2)
print("\nResult:")
print(list(result))