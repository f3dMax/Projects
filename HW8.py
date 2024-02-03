# HW8.py
# Author: Maksym Fedenko

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button
st.title("Simple Date Counter App")
# 4. Create a subheader for the web application
st.subheader("Enter a date to calculate days from today")

# 5. Create a date input for the user
user_date = st.date_input("Choose a date")

# 6. Create a button for the user to click
button_clicked = st.button("Calculate Days")



# The calculate_days function from Lab9.py
def calculate_days(target_date):
    # Get the current date
    current_date = dt.date.today()
    # Calculate the difference
    difference = target_date - current_date
    # Return the number of days
    return difference.days


# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.

def calculate_days_until_birthday(birthday):
    today = dt.date.today()
    next_birthday = dt.date(today.year, birthday.month, birthday.day)
    if today > next_birthday:
        next_birthday = dt.date(today.year + 1, birthday.month, birthday.day)
    days_until_birthday = (next_birthday - today).days
    st.write(f"Days until your next birthday: {days_until_birthday}")
    return days_until_birthday


# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
def days_until_semester_ends():
    today = dt.date.today()
    end_of_semester = dt.date(2023, 12, 8)  # Modify the year and date as needed
    days_until_end = (end_of_semester - today).days
    st.write(f"Days until the end of the semester: {days_until_end}")
    return days_until_end

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")

def days_until_new_years():
    today = dt.date.today()
    new_years = dt.date(today.year + 1, 1, 1)
    days_until_new_year = (new_years - today).days
    st.write(f"Days until New Year's Day 🎉: {days_until_new_year}")
    return days_until_new_year

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

birthday = st.date_input("Enter your birthday")
if st.button("Calculate Days Until Birthday"):
    calculate_days_until_birthday(birthday)

if st.button("Days Until Semester Ends"):
    days_until_semester_ends()

if st.button("Days until New Year's Day"):
    days_until_new_years()


# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py
def run_app():
    # Check if the button has been clicked
    if button_clicked:
        try:
            # Call the calculate_days function
            days_until = calculate_days(user_date)
            # Print the result
            st.write(f"Days until {user_date}: {days_until}")
        except Exception as e:
            st.error("An error occurred: " + str(e))



if __name__ == '__main__':
    run_app()