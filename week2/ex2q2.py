from hashlib import sha3_224


def mirror(a,b):
    rev=a[::-1]
    if(b==rev):
        print("True")
    else:
        print("False")
s1=input("Enter The first Word")
s2=input("Enter the second Word")
mirror(s1,s2)            