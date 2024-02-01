# Project1.py
# Author:Maksym Fedenko


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_screen():
    print ("Welcome to the quiz game!!! In this game I am going to give you five questions with four answers, try to get them all right. Good Luck!")


# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct
def ask_question(question, answers, correct_answer):
    print(question)
    for key, value in answers.items():
        print(f"{key}: {value}")
    while True:
        user_answer = input("Your answer (a, b, c, d): ").lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            if user_answer == correct_answer:
                print("Correct! You've earned a point.")
            else:
                print(f"Incorrect. The correct answer was '{correct_answer}'.")
            return user_answer == correct_answer
        else:
            print("Invalid input. Please enter a, b, c, or d.")


def display_score(score):
    print(f"Your final score is {score} out of {len(questions)}. Thank you for playing!")

welcome_screen()



questions = [
    {
        'question': "What is the capital of Portugal?",
        "answers": {'a': "Benin", 'b': 'Lisbon', 'c': 'Paris', 'd': 'Manchester'},
        "correct": "b"
    },
    {
        "question": "What is 77 + 33?",
        "answers": {'a': '100', 'b': '101', 'c': '120', 'd': '110'},
        "correct": "d"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": {'a': 'Earth', 'b': 'Mars', 'c': 'Jupiter', 'd': 'Venus'},
        "correct": "b"
    },
    {
        "question": "In what year did World War I begin?",
        "answers": {'a': '1914', 'b': '1916', 'c': '1918', 'd': '1915'},
        "correct": "a"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "answers": {'a': 'Atlantic Ocean', 'b': 'Indian Ocean', 'c': 'Arctic Ocean', 'd': 'Pacific Ocean'},
        "correct": "d"
    },
]

score = 0
# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).



for question in questions:
    if ask_question(question['question'], question['answers'], question['correct']):
        score += 1

# Display the final score
display_score(score, len(questions))

