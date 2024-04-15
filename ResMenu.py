# You own a restaurant with five food dishes, organized in the Python list menu below. One day, you decide to:

#? remove bean soup ('bean soup') from the menu, and
#? add roasted beet salad ('roasted beet salad') to the menu.

menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp', 'fish soup with cream and onion', 'gyro']

# Remove 'bean soup' from the menu and add the 'roasted beet salad' to the end of the menu.
menu.remove('bean soup')
menu.append('roasted beet salad')

print(menu) # Print the updated list of menu items
