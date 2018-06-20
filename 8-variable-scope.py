x = 6
y = 7
def example():
    global x
    z = 5
    print(x)
    print(x+5)
    x+=6
    print(x)

example()

def example2():
    globy = y

    globy+=7
    return globy

returnedVal = example2()
print(returnedVal)
