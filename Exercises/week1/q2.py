import random
value=random.randint(1,9)
def choice():
    x=int(input('Enter your number '))
    if(x==value):
        print('Well done...')
    else:
        choice()
print('Computer guessed a random number:-')
choice()




