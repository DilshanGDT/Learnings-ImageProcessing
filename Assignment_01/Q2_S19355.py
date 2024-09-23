
def fac(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial 

def user_input():
    num = input('Enter a valid Number - ')

    if(num.isdigit()):
        print(f'{num}! = {fac(int(num))}')
    else:
        print('Invalid Input...! Try Agian using positive Numerics')

user_input()
