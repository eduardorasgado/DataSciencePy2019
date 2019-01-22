# dictionary
# dictionary has key and values
# are denoted with curly brackets {}
#the values can be inmutable, mutable and duplicates
# the keys have to be inmmutable and unique
# each key and value pair is separated by a comma

ids_dict = {
    "Fernando": "AA4P33",
    "Gabriel": "45D113",
    "Ann": "1A2ACX",
    "Laura": "5TTE1A"
}

for key, value in ids_dict.items():
    print("key: {}, value: {}".format(key, value))

some_dict = {
    "key1": 1,
    "key2": "2",
    "key3": [3,4,5],
    "key4": (8,6,9),
    ("key5", "key5.2"): 5
}

def show_dict(some_dict):
    for key, value in some_dict.items():
        print("{}: {}".format(key, value))

show_dict(some_dict)

# accessing a value given a key
print(some_dict["key3"])
# in reserved word
print("key4" in some_dict)

# adding a new element to dictionary
print("-------")
some_dict["key6"] = 8.3
show_dict(some_dict)
#accessing just to dictionary keys
print("Keys: ")
print(some_dict.keys())
print("Values: ")
print(some_dict.values())