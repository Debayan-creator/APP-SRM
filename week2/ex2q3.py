import random
def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0,1))
        key1 += temp
    return(key1)
n=8
str1 = rand_key(n)
print("length random binary string is: ",str1)
        
