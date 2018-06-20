#import statistics as s
#from statistics import variance, mean
#from statistics import variance as v, mean as m
from statistics import *
example_list = [1,3,4,4,4,5,5,6,7,8,8,9,5,4,4]

#x = s.variance(example_list)
# x = variance(example_list)
# y = mean(example_list)
#x = v(example_list)
#y = m(example_list)
x = mode(example_list)
y = variance(example_list)

print(x)
print(y)
