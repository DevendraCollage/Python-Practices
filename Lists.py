# When doing data science, you need a way to organize your data so you can work with it efficiently. Python has many data structures available for holding your data, such as lists, sets, dictionaries, and tuples. In this, you will learn how to work with Python lists.

#* Demo of the store the string data in simple format

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers)) # Output: <class 'str'>
print(flowers)

#* Even better is to represent the same data in a Python list. To create a list, you need to use square brackets ([, ]) and separate each item with a comma. Every item in the list is a Python string, so each is enclosed in quotation marks.

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list)) # Output: <class 'list'>
print(flowers_list)

#* At first glance, it doesn't look too different, whether you represent the information in a Python string or list. But as you will see, there are a lot of tasks that you can more easily do with a list. For instance, a list will make it easier to:

#? get an item at a specified position (first, second, third, etc),
print(flowers_list.index("canterbury bells")) # Output: 2

#? check the number of items.
print(len(flowers_list)) # Output: 10

#? add and remove items.
flowers_list.append("hello world") #* This will add the new item in the end of the list
print(flowers_list)
flowers_list.remove("hello world") #* This will remove the added of the list
print(flowers_list)

#TODO: Perform Some of the Operations on the list and use the some built-in method

#! 1. Length
#* We can count the number of entries in any list with len(), which is short for "length". You need only supply the name of the list in the parentheses.
print(len(flowers_list)) # Output: 10

#! 2. Indexing
#* We can refer to any item in the list according to its position in the list (first, second, third, etc). This is called indexing.
#* Note that Python uses zero-based indexing, which means that:

#? to pull the first entry in the list, you use 0,
#? to pull the second entry in the list, you use 1, and
#? to pull the final entry in the list, you use one less than the length of the list.
print("First entry:", flowers_list[0]) # Output: "pink primrose"
print("Second entry:", flowers_list[1]) # Output: "hard-leaved pocket orchid"
# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9]) # Output: "globe thistle"

#! 3. Slicing
#* You can also pull a segment of a list (for instance, the first three entries or the last two entries). This is called slicing. For instance:
#? to pull the first x entries, you use [:x], and
#? to pull the last y entries, you use [-y:].
print(flowers_list[0:3]) # This will return three flowers name of the list
# As you can see above, when we slice a list, it returns a new, shortened list.

#! 4 Removing Items
#* Remove an item from a list with .remove(), and put the item you would like to remove in parentheses.
flowers_list.remove("globe thistle") #* This will remove the from of the list
print(flowers_list)

#! 5 Adding Items
#* Add an item to a list with .append(), and put the item you would like to add in parentheses.
flowers_list.append("hello world") #* This will add the new item in the end of the list
print(flowers_list)

#! Lists are not just for strings
#* So far, we have only worked with lists where each item in the list is a string. But lists can have items with any data type, including booleans, integers, and floats.
#* As an example, consider hardcover book sales in the first week of April 2000 in a retail store.
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
# Here, hardcover_sales is a list of integers. Similar to when working with strings, you can still do things like get the length, pull individual entries, and extend the list.
print(len(hardcover_sales)) # Output: 7
hardcover_sales.append(45) # Add at the end of the list
print(hardcover_sales)
print("Minimum:", min(hardcover_sales)) # Output: 45
print("Maximum:", max(hardcover_sales)) # Output: 191
print("Total books sold in one week:", sum(hardcover_sales)) # Output: 1152

#* We can also do similar calculations with slices of the list. In the next code cell, we take the sum from the first five days (sum(hardcover_sales[:5])), and then divide by five to get the average number of books sold in the first five days.
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5) # Output: 153.8