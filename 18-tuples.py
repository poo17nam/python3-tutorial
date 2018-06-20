# tuples are immutable

x = 5,6,2,6

y = [5,6,2,6]

print(x[1])
print(y[1],y[2])

# tuples are mainly used for sequence unpacking

def example():
    return 8,16

(x,y) = example()

print(x,y)
