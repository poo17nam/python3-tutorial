def example():
    print('basic function')
    x = 3 + 5
    print(x)

example()

def simple_addition(num1,num2):
    answer = num1+num2
    print('\nnum1 : ' ,num1)
    print(answer)

#simple_addition(7,8)
simple_addition(num2=4,num1=1)

#default function parameters
def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print('\n',num1,num2)

simple(2)


def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc,scrollbar)

basic_window(500,400,bgc='b')
