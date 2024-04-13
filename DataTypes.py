# We will explore the Data Types of the Python Available.

#? 1. Integer
#* Integers are numbers without any fractional part and can be positive (1, 2, 3, ...), negative (-1, -2, -3, ...), or zero (0).
x = 10
print(x) # Output: 10
print(type(x)) # Output: <class 'int> (<class 'int'> refers to the integer data type.)

#? 2. Float
#* Floats are numbers with fractional parts. They can have many numbers after decimal.
y = 10.2514
print(y) # Output: 10.2514
print(type(y)) # Output: <class 'float'> (<class 'float'> refers to the float data type.)

#! We can also define the float with fractional 
almost_pi = 22/7
print(almost_pi) # Output: 3.1428.......
print(type(almost_pi)) # Output: <class 'float'> (<class 'float'> refers to the float data type.)

#! One function that is particularly useful for fractions is the round() function. It lets you round a number to a specified number of decimal places.
# Round to 5 decimal places
rounded_pi = round(almost_pi, 4)
print(rounded_pi) # Output: 3.1429
print(type(rounded_pi))

#? 3. Boolean
#* Booleans represent one of two values: True or False. In the code cell below, z_one is set to a boolean with value True.
z_one = True
print(z_one) # Output: True
print(type(z_one)) # Output: <class 'bool'>

z_two = False
print(z_two) # Output: False
print(type(z_two)) # Output: <class 'bool'>

#! Booleans are used to represent the truth value of an expression. Since 1 < 2 is a true statement, z_three takes on a value of True.
z_three = (1 < 2)
print(z_three) # Output: True
print(type(z_three)) # Output: <class 'bool'>

z_four = (5 < 3)
print(z_four) # Output: False
print(type(z_four)) # Output: <class 'bool'>

#! We can switch the value of a boolean by using not. So, not True is equivalent to False, and not False becomes True
z_five = not z_four
print(z_five) # Output: True
print(type(z_five)) # Output: <class 'bool'>

#? 4. String
#* The string data type is a collection of characters (like alphabet letters, punctuation, numerical digits, or symbols) contained in quotation marks. Strings are commonly used to represent text.
w = "Hello, Python!"
print(w) # Output: Hello, Python!
print(type(w)) # Output: <class 'str'>

#! You can get the length of a string with len(). "Hello, Python!" has length 14, because it has 14 characters, including the space, comma, and exclamation mark. Note that the quotation marks are not included when calculating the length.
strLen = len(w)
print(strLen)

#! One special type of string is the empty string, which has length zero.
shortest_string = ""
print(type(shortest_string)) # Output: <class 'str'>
print(len(shortest_string)) # Output: 0

#! If you put a number in quotation marks, it has a string data type.
my_number = "1.12321"
print(my_number) # Output: 1.12321
print(type(my_number)) # Output: <class 'str'>

#! Convert a String into Number (integer, float)
also_my_number = float(my_number)
print(also_my_number) # Output: 1.12321
print(type(also_my_number)) # Output: <class 'float'>