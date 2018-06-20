# lists are mutable

x = [3,4,5,6,7,6,4,3,2,2,1,6,8,9,9,6,7,5,4]

x.append(2) # adds the value specified to end of list
print("After appending 2:",x)

x.insert(2,99) # Insert 99 at 2nd position
print(x)

x.remove(4) # removes the value 4 from list
print(x)

x.remove(x[4])  # removes value at index 4
print(x)

print(x[5:9])   # slices elements from 5th to 8th position

print(x[-1]) # gives last element of list
print(x[-2]) # gives second last element of list

print(x.index(1)) # to get the index of value 1 in list

print(x.count(6)) # gives number of element 6 present in list

x.sort()
print(x)

y = ['Janet','Alice','Bob','Joe']

y.sort()
print(y)
