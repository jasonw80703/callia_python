# Lists again!
my_list = [1, 2, 3]
# pets = ["dog", "cat", "fish"]
# my_pets = ["dog", "cat", "fish"]
# print(pets == my_pets)
# Order - lists are ordered, meaning one item comes after the other
# print the length of pets (or the number of pets)
# print(len(pets))

# Indexing
# Lists are indexed, you can access items in the list using numbers.
pets = ["dog", "cat", "fish", "bunny"]

# THIS IS VERY IMPORTANT
# in computer science, or programming, we count from 0
# In normal life, we count from 1.

# Get (access) the first item in the pets list.
# We should use the number 0.
# print(pets[0])
# Get (access) the second item in the pets list.
# We should use the number 1.
# print(pets[1])
# Get (access) the third or last item in the pets list.
# We should use the number 2.
# print(pets[2])

fruits = ["apple", "banana", "orange", "pineapple", "grape"]
# Get (access) "orange" from the list fruits.
# 2 is the index we're using.
# print(fruits[2])

# print(fruits)
# Example: to change something at the index 1
fruits[1] = "durian"
# Change the "fish" in pets list to "bird".
pets[2] = "bird"
# Change the "dog" in pets list to 5.
pets[0] = 5
# print(pets)

# Print pets at index 3 when the length is only 3.
# This creates an error.
# print(pets[3])

# Quiz
################################
# Question 1
# Create a list called colors that has 5 colors in it.
colors = ["blue", "purple", "pink", "green", "yellow"]
################################
# Question 2
# Get (access) your favorite color from that list and print it.
print(colors[1])
################################
# Question 3
# Get (access) your least favorite color from that list and change it to another color.
colors[3] = "red"
print(colors)
################################
# Question 4
# Get (access) the 5th index of your list. What do you think it will return?
print(colors[5])
