# HW3.py
# Author: Maksym Fedenko

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def square_number():
    num = int(input("Enter a number: "))  # Allows for both integer and decimal inputs
    squared_num = num ** 2
    print(f"The square of {num} is {squared_num}")
    return squared_num

result = square_number()

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
def replace_letter():
    string = input("Enter a string: ")
    letter = input("Enter a letter to insert: ")
    index = int(input("Enter the index to replace the letter at: "))
    new_string = string[:index] + letter + string[index + 1:]
    print(f"Modified string: {new_string}")
    return new_string

result = replace_letter()
# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
def is_within_bounds():
    number = float(input("Enter a number: "))
    lower = float(input("Enter the lower bound: "))
    upper = float(input("Enter the upper bound: "))
    within_bounds = lower <= number <= upper
    print(f"Is the number within bounds: {within_bounds}")
    return is_within_bounds

result = is_within_bounds()
# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function
def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    return name, age, color

def print_user_info(name, age, color):
    print(f"Hello, my name is {name}. I am {age} years old. My favorite color is {color}.")

name, age, color = get_user_info()
print_user_info(name, age, color)
# Question 5:
# import the random module and use it to generate a random number between 1 and 100
import random

def generate_random_number():
    rand_num = random.randint(1, 100)
    print(f"Random number between 1 and 100: {rand_num}")
    return rand_num
generate_random_number()
# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math

def find_sqrt():
    number = int(input("Enter a number to find the square root: "))
    sqrt_number = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_number}")
    return sqrt_number
find_sqrt()
# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system

def display_python_version():
    print("Python version:", system.version)


display_python_version()
# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
from os import getcwd as current_working_directory

def display_cwd():
    cwd = current_working_directory()
    print("Current working directory:", cwd)
    return cwd
display_cwd()
