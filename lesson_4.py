# Review from last week
# ======
# Booleans
# True and False
# print(True)
# print(False)

# Operators
# +, -, *, /
# Equals
# ==
# Greater than
# >
# print(5 > 3) should be True
# Less than or equals
# <=
# print(3 <= 3) should be True
# print(3 < 3) should be False
# !=
# This is not equal.
# print(3 != 6) should be True
# print(5 != 5) should be False

# This week
# =========
# Lists

# What is a list?
# A list is a collection of items.
# For example, you can have a list of groceries, a list of things to do, a list of classes, etc.
# Lists use [] (square brackets)

# Example
# the name of the variable is a, the value is 5
a = 5
# can you create a variable named b, value as the list [1,2, 3]
b = [1, 2, 3]
animals = ['cat', 'tiger', 'lion']
# print(animals)
# What can be inside a list?
# Answer: you can put anything in lists.
# You can put numbers, strings, booleans, lists.
Bool = [True, False]
l = [b, animals, Bool]
# print(l)

# Length of a list - how many items are inside the list
# To get the length of a list, use len(), and you put the list inside
# print(len(animals)) # will return 3
# print(len(Bool))
# print(len(b))

# To get the number of items (length) of a list, use
# len()

# Quiz
# ====
# 1. For each person in your family, create a variable with their name.
# 2. Create a list with all the names of your family.
# 3. Print the list.
# 4. Print the length of the list.
first = "Ed"
second = "Sharon"
third = "Callia"
fourth = "Lucas"
family = [first, second, third, fourth]
# print(family)
print(len(family) + 5)
