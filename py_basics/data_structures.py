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

data_t = (10, 9, 6, 5, 10, 8, 9, 2, 3, 4, 0, 11)
print(data_t)

sorted_data = sorted(data_t, reverse=True)
print(sorted_data)

print("---------------")

# tuples inside a tuple: nesting
tuples_t = (1, 2, ("pop", "rock"),
    (10, 20, ("hello", "bye", ("a", "b", "c", 7000, 8000))),
    ("disco", (5.3, 6.5)), 5.44)

def tuple_in_tuple(my_tuple):
    """ printing elements not a tuple, if it is a tuple
        then call function recursively
    """
    for i in range(len(my_tuple)):
        if(type(my_tuple[i]) == tuple):
            tuple_in_tuple(my_tuple[i])
        else:
            print(my_tuple[i])

tuple_in_tuple(tuples_t)