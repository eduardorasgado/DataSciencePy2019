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