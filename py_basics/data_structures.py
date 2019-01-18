# LIST AND TUPLES

#Tuples
# it is inmutable 
ratings = (10, 10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1)
for i in range(len(ratings)):
    print(ratings[i])

print("-------------------")
# cannot do this
#ratings[2] = 11

tuple1 = ("size", 800, 600)

# accessing elements using negative index
for i in range(len(ratings)):
    neg_i = -len(ratings) + i
    #print(neg_i)
    print(ratings[neg_i])


print("-----------------")
# concatenating tuples
twice_pow = (15, 14, 13, 12, 11) + ratings
for i in twice_pow:
    print(i)

#slicing tuples
print(twice_pow[3:9])

# printing loop with intervals in tuples
for i in twice_pow[::2]:
    print(i)

