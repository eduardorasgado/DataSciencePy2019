#sets
#sets are like lists and tuples

# sets are unordered
# sets have only unique elements

music_set = {"pop", "rock", "rock", "soul", "hard rock", "R&B", "Disco"}

print(music_set)

# we can convert from list to set by applying a type
#casting like this
my_list = [1,2,3,4,5,6,7,8,9,9]
print(my_list)

my_set = set(my_list)
print(my_set)

# set operations
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(A)
# set union
A = A ^ B
print(A)

# adding just one element to the set
A.add(11)
print(A)

# remove an item from a given set
A.remove(1)

# "in" command to check if a set has a value
print("1 is in A: {}".format(1 in A))
print("2 is in A: {}".format(2 in A))

# mathematical operations between sets
men_set = {"Eduardo", "Mariano", "John", "Carl", "Chalino"}
women_set = {"Monica", "Luisa", "Cher", "Daniela", "Chalino"}
# union operation: drops the repeated element in both sets
mix_set = men_set ^ women_set
mix_set.pop()
mix_set.pop()
print(mix_set)

# intersection operation: keeps the repeated element in both sets
mix2 = mix_set & men_set
print(mix2)

# issubset operation: if men_Set is contained by mix_set
print("issubset: ",men_set.issubset(mix_set))
# checking superset: if mix_set contains men_Set
print("is super set: ", mix_set.issuperset(men_set))

# difference
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9,10}
# find the difference in set1 but not set2
print(set1.difference(set2))
# now reverse
print(set2.difference(set1))