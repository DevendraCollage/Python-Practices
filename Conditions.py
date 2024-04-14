# Conditions

#* In programming, conditions are statements that are either True or False. There are many different ways to write conditions in Python, but some of the most common ways of writing conditions just compare two different values. For instance, you can check if 2 is greater than 3
print(2>3) # Python identifies this as False, since 2 is not greater than 3.

#* You can also use conditions to compare the values of variables. In the next code cell, var_one has a value of 1, and var_two has a value of 2. In the conditions, we check if var_one is less than 1 (which is False), and we check if var_two is greater than or equal to var_one (which is True).
var_one = 1
var_two = 2

print(var_one < 1) # Output: False
print(var_two >= var_one) # Output: True

#* For a list of common symbols you can use to construct conditions, check out the chart below.

#! Symbol	Meaning
#!  ==	    equals
#!  !=	    does not equal
#!  <	    less than
#!  <=	    less than or equal to
#!  >	    greater than
#!  >=	    greater than or equal to

#* Conditional statements
# Conditional statements use conditions to modify how your function runs. They check the value of a condition, and if the condition evaluates to True, then a certain block of code is executed. (Otherwise, if the condition is False, then the code is not run.)

#? 1. Simple if
#* The simplest type of conditional statement is an "if" statement. You can see an example of this in the evaluate_temp() function below. The function accepts a body temperature (in Celsius) as input.
#! Function what should do explain below: 
# Initially, message is set to "Normal temperature".
# Then, if temp > 38 is True (e.g., the body temperature is greater than 38°C), the message is updated to "Fever!". Otherwise, if temp > 38 is False, then the message is not updated.
# Finally, message is returned by the function.

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

#* ⬆️ Note that there are two levels of indentation ⬆️:
#? The first level of indentation is because we always need to indent the code block inside a function.
#? The second level of indentation is because we also need to indent the code block belonging to the "if" statement. (As you'll see, we'll also need to indent the code blocks for "elif" and "else" statements.)

# Call the function
print(evaluate_temp(37)) # Output: Normal temperature
print(evaluate_temp(39)) # Output: Fever!

#? 2. if-else statements
# We can use "else" statements to run code if a statement is False. The code under the "if" statement is run if the statement is True, and the code under "else" is run if the statement is False.

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

# Call the function
print(evaluate_temp_with_else(20)) # Output: Normal temperature
print(evaluate_temp_with_else(45)) # Output: Fever!

#? 3. if-elif-else statements
#* We can use "elif" (which is short for "else if") to check if multiple conditions might be true. The function below:

# First checks if temp > 38. If this is true, then the message is set to "Fever!".
# As long as the message has not already been set, the function then checks if temp > 35. If this is true, then the message is set to "Normal temperature.".
# Then, if still no message has been set, the "else" statement ensures that the message is set to "Low temperature." message is printed.

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

# Call the function
print(evaluate_temp_with_elif(34)) # Output: Low Temperature.
print(evaluate_temp_with_elif(42)) # Output: Fever!
print(evaluate_temp_with_elif(37)) # Output: Normal Temperature.

#? Example - Calculations
#* In this next example, say you live in a country with only two tax brackets. Everyone earning less than 12,000 pays 25% in taxes, and anyone earning 12,000 or more pays 30%. The function below calculates how much tax is owed.

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed
    
# Call the function    
print(get_taxes(15450)) # Output: 4635.0
print(get_taxes(9500)) # Output: 2375.0
