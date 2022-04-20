def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=" ")
        print('\r')

def pattern2(n):
    for i in range(5,0,-1):
        for j in range(0,i-1):
            print('*',end=" ")
        print('\r')

pattern(5)
pattern2(5)