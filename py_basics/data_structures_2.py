# ----------------------------------------------------------
# LISTS
# List are also ordered sequences
# a list are represented with square brackets
# list are mutables

my_list = ["Michale", "Jackson", 10.4, True, 1455]

for i in range(len(my_list)):
    print(i)

print("------------------")
# lists can contain elements whatever you need, they can contain
# nested elements, including tuples and more lists

mix_list = ["Eduardo", "Rasgado", 10.1212, 1224, [1,2,3,4,5], ('A', 12), (22, 45)]

for i in range(len(mix_list)):
    print(mix_list[i])

print("---------------------")
# printing lists using negative index
for i in range(len(mix_list)):
    neg = -len(mix_list) + i
    print(mix_list[neg])

# list slicing
print("Slicing: ")
print(mix_list[::2])
print(mix_list[3:5])

# adding or concatenating lists
print("Concatenating: ")
list_2 = [1,2,3,4,5,6,7,8]
new_list = sorted(list_2, reverse=True) + mix_list
for i in new_list:
    print(i)

# instead of creating a new list we can work with the original one
new_list.extend(["PooP", "___", 10, "0xFF"])

for i in new_list:
    print(i, end=" ")
print("\n")