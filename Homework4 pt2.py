#Use the DateTime module to get Current Date and Time, and save it to a variable. 
#Then extract just the Full month name form that variable.

import datetime

current_datetime = datetime.datetime.now()

full_month_name = current_datetime.strftime("%B")

print("Current date and time:", current_datetime)
print("Full month name:", full_month_name)

#Write a simple function that takes 2 parameters -- a  first name and a day name.
    #- Set a default value for the day name of Sunday.
    #- Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.  
    #- Invoke this function with 2 variables.
    #- Invoke this function with 1 variable only.

def greet(first_name, day_name="Sunday"):
    print(f"Hi {first_name}! Happy {day_name}!")

greet("Alice", "Wednesday")
greet("Bob", "Friday")

greet("Charlie")


#Write a block of code to handle one of the most common Python exception errors. Select one of the common errors from the curriculum section on
#Python Exception handling. Have your code example uses the `try`,`except`, `else`, and `finally` components.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    result = numerator / denominator

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
else:
    print("Result:", result)

finally:
    print("This will always be executed, regardless of whether an exception occurred or not.")
