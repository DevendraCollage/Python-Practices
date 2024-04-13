# Write a function get_expected_cost that returns the expected cost of producing n units of a house.
#* the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
#? each bedroom adds 30000 to the expected cost,
#? each bathroom adds 10000 to the expected cost, and
#? a basement adds 40000 to the expected cost.

def get_expected_cost(beds, baths, has_basement):
    value = (beds * 30000 + baths * 10000 + (40000 if has_basement else 0) + 80000)
    return value;

print(get_expected_cost(1,2, True)) # Output: 170000