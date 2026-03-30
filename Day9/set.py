#set in python
s = {}
type (s)
my_set = {1, 2, 3, 4}
my_set = set([1, 2, 3, 4])
{1, 2, 2, 3}   # Output: {1, 2, 3} no duplicate
#Common operations
my_set.add(5)
#Remove elements
my_set.remove(3)   # error if not found
my_set.discard(10) # no error if not found
#Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}
print(a - b)  # Difference → {1, 2}

#Check membership
print(2 in a)  # True
#Empty set (important!)
empty = set()   # correct
empty = {}      # WRONG → creates a dictionary
#Add elements
a.add(6)
print(a)
#Update (Add multiple elements)
a.update([7, 8])
print(a)
 #Remove elements
a.remove(2)    # error if not present
a.discard(10)  # no error
#Pop (Remove random element)
a.pop()
#Clear (Remove all elements)
a.clear()
#Subset & Superset
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True
#Membership check
print(3 in a)    # True