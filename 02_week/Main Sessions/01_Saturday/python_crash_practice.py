# *Start of Python*

# Print the line
print("Hello World")

# Comments
# this is comments

# Variables
x = 20
print(x)
print(type(x))

y = 50.6
print(y)
print(type(y))

z = "Umair"
print(z)
print(type(z))

# Arithmetic Operators
a = 10
b = 20

print("a", a)
print("b", b)
print("a + b", a + b)
print("a - b", a - b)
print("a * b", a * b)
print("a / b", a / b)
print("a // b", a // b)
print("a % b", a % b)
print("a ** b", a**b)

#
f = 40
F = 50
print("f", f)
print("F", F)

# boolean Operators
r = True
s = False
t = True

print("r", r)
print("type(r)", type(r))
print("s", s)
print("type(s)", type(s))
print("t", t)
print("type(t)", type(t))

print("r and s", r and s)
print("r and t", r and t)
print("r or s", r or s)
print("r or t", r or t)
print("not r", not r)
print("not s", not s)


# Comparison Operators

h = 10
i = 20
j = 15

print("h", h)
print("i", i)
print("h == i", h == i)
print("h != i", h != i)
print("h > i", h > i)
print("h < i", h < i)
print("h >= i", h >= i)
print("h <= i", h <= i)

# if
if h > i:
    print("h is greater than i")

if h < i:
    print("h is less than i")

# if else
if h > i:
    print("h is greater than i")
else:
    print("h is less than i")


# if elseif else
if h > j:
    print("h is greater than j")
elif h == j:
    print("h is equal to j")
else:
    print("h is less than j")


# Loops

# for loop
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# reverse loop
for i in range(10, 0, -1):
    print(i)

# index based loop

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# value based loop
for fruit in fruits:
    print(fruit)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

# reverse loop
i = 10
while i > 0:
    print(i)
    i -= 1


# Built in functions
num = [56, 23, 45, 78, 12, 90, 34, 67, 89, 23]
print("num", num)
print("max(num)", max(num))
print("min(num)", min(num))
print("sum(num)", sum(num))
print("len(num)", len(num))
# print("sorted(num)", sorted(num))
# print("sorted(num, reverse=True)", sorted(num, reverse=True))
# print("sorted(num, reverse=False)", sorted(num, reverse=False))


# Method or Function
def add(u, v):
    ans = u + v
    print("ans", ans)
    return ans


add(10, 20)

# Lists
# List is a collection which is ordered and changeable. Allows duplicate members.
#                .....,-4,-3,-2,-1
#       0, 1, 2, 3, 4, .......
list = ["apple", "banana", "cherry", 94, 45.6, True, False, 45, 67, 89, 34.43]
print("list", list)
print("type(list)", type(list))
print("len(list)", len(list))
print("list[0]", list[0])
print("list[6]", list[6])

for i in list:
    print(i)

for i in range(len(list)):
    print(i, list[i])


# Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
tuple = ("apple", "banana", "cherry", 94, 45.6, True, False, 45, 67, 89, 34.43)
print("tuple", tuple)
print("type(tuple)", type(tuple))
print("len(tuple)", len(tuple))
print("tuple[0]", tuple[0])
print("tuple[6]", tuple[6])
# change not allowed
# tuple[0] = "orange"

# Set
# Set is a collection which is unordered and unindexed. No duplicate members.
# set loop have no index

Set = {5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 6, 6}
print("Set", Set)

# Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# dictionary have key value pair
# dictionary loop have key
dict = {
    "name": "John",
    "age": 36,
    "city": "Faisalabad",
    "country": "Pakistan",
    "marks": [56, 78, 90, 45, 67],
}
print("dict", dict)
# get value by key
print("dict['name']", dict["name"])
print("dict['age']", dict["age"])
print("dict['city']", dict["city"])
print("dict['country']", dict["country"])
print("dict['marks']", dict["marks"])

# get all keys
for i in dict:
    print(i)

# get all values
for i in dict:
    print(dict[i])

# get all keys and values

for key, value in dict.items():
    print(key, value)
