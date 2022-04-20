def remv(char2):
    if char2.isdigit() or char2.isalpha():
        print(char2,end="")

str=input("Enter string:")
for i in str:
    remv(i)