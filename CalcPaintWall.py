# We are calculate the price of the paint the wall as par house size

#* 1. Define the function
#? sqft_wall : total square feet of walls to be painted
#? sqft_ceiling = square feet of ceiling to be painted
#? sqft_per_gallon = number of square feet that you can cover with one gallon of paint
#? cost_per_gallon = cost (in dollars) of one gallon of paint

def get_cost(sqft_walls,sqft_ceiling,sqft_per_gallon,cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost 

#* Call the function and pass the value
passValue = get_cost(432, 144, 400, 15)
print(passValue) # Output: 21.5999999999999998