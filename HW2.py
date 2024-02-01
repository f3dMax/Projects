# HW2.py
# Author: Maksym Fedenko


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

age = int(input("Enter your age "))

if age <= 13:
    print("You are a child ")
elif 13 < age <= 19:
    print("You are a teenager ")
elif age >= 20:
    print("You are an adult ")
# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
rows = 5


for i in range(1, rows + 1):
    
    for j in range(1, i + 1):
        print(j, end="")
    
    print()
# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.
# Initialize an empty list to store the numbers
numbers = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

highest = max(numbers)
lowest = min(numbers)
average = sum(numbers) / len(numbers)

print(f"The highest number is: {highest}")
print(f"The lowest number is: {lowest}")
print(f"The average of the numbers is: {average}")

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
# Initialize an empty list to store the numbers
# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Convert the string to lowercase
lowercase_string = user_input.lower()

# Initialize a counter for vowels
vowel_count = 0

# List of vowels
vowels = "aeiou"

# Loop over each character in the string
for char in lowercase_string:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1

# Display the number of vowels
print(f"The number of vowels in the string is: {vowel_count}")
