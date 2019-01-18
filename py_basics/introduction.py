# this is a commend
print("This is my first code line in python 3")

#types in python
my_data = [1.2, 1.3, 1.4, 1.5, 1.6]

for i in my_data:
    print(i)

print("This is a string")
# castings
x = 24
y = float(x)
print(y)

print(type(True))

is_checked = True
is_c_int = int(is_checked)
print(is_c_int)

# expressions and variables
arithmetic = 34+54+34+34 * 5.0
print(arithmetic)

print("Float division: ")
print(25/6)

print("Integer division: ")
print(25//6)

# order operation
print((2 * 60) + 30)

x = 25
print(x)

x = x/5
print(x)

# strings

name = "Michael Jackson"

print(name)
print(name[1])

# getting last element in name
print(name[-1])
print(name[-2]+ "\n")

# lets do something using string
some_name = "Eduardo Rasgado Ruiz"

for i in range(len(some_name)):
    # printing some-name in a reverse way
    print(some_name[len(some_name)-i-1])

print("-----------------\n")

for i in range(len(some_name)):
    reverse_num = -len(some_name) + i
    print(some_name[reverse_num])
    #print(reverse_num)


# getting just a range from string: slicing

#getting first place in which space is
space = 0
for i in range(len(some_name)):
    if some_name[i] == " ":
        space = i
        break;
print("space is {}".format(space))
print(some_name[0:7])

# STRIDE: slicing with a range
# printing each 2 letters
print(some_name[::2])

#printing each 2 lette until get the 7th element in the string
print(some_name[:7:2])

somename_3 = some_name*3
print(somename_3)

# strings in python are inmutable
# this is permitted
some_name = "ssssss"
print(some_name)

#this is not
#some_name[3] = "s"

# Escape sequences

print("Mozart is \tthe best")
print("Mozart is \n the best")
print("Mozart is \\the best")
print(r"Mozart is the best")

# STRING METHODS =======================
print("--------------------------------")
#Sequence methods and string methods

a_good_phrase = "Thriller us the sxth studio album"

# split method
print("Split: ")
phrase_list = a_good_phrase.split(" ")
for i in phrase_list:
    print(i)

# join method
print("Join: ")
phrase_string_again = " ".join(phrase_list)
print(phrase_string_again)

# upper method
print("Upper: ")
upper_phrase = a_good_phrase.upper()
print(upper_phrase)

print("LOwer: ")
lower_phrase = upper_phrase.lower()
print(lower_phrase)

#replace
print("Replace method: ")
# to be replace, new value to be assigned
replaced_phrase = a_good_phrase.replace(" ", "-")
print(replaced_phrase)

name = "Eduardo Rasgado"

#find
print("Find: ")
found_e = name.find("as")

print(found_e)

if found_e != -1:
    print(name[found_e:11])
else:
    print("NOT FOUND")