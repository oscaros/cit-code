from typing import Union


empty_set = set()
mylist = [1,1,2,3,4]

#removing duplicates from a list
print(set(mylist))

#modifying a set #sets are mutable and un ordered
#therefore we cannot update or set using indexing or slicing
empty_set.add(2)#adds one value
print(empty_set)

#adding multiple
empty_set.update(mylist)
print(empty_set)

#removing items
empty_set.remove(3) #raises error if 3 is not found
empty_set.discard(3)

#pop method removes random element
#clear method clears all

#union of sets
new_set = {"osc"}
print(empty_set | new_set) 

#or
print(empty_set.union(new_set)) 

#intersection of sets
setA = {1,2,3}
setB = {1,4,5}
print(setA & setB) 
print(setA.intersection(setB)) 

#diffrence of sets
print(setA - setB) 
print(setA.difference(setB)) 

#sets symmetric difference
print(setA ^ setB) 
print(setA.symmetric_difference(setB)) 

