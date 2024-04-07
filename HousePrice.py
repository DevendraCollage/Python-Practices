# Write a function that is get two arguments from the function 
#* This function is predict the price of the house on the based on no of bad and bathroom.
#? For 1 bedroom price = 30000
#? For 1 bathroom price = 10000
#? For house with 0 bedroom and 0 bathroom = 80000

#todo: You can also write like this function and this is complex way
# def get_expected_cost(beds, baths):
#     # price = beds + baths * ()
#     if beds == 0 and baths == 0 : return  80000
#     elif beds > 0 and baths < 0 : return (beds * 30000) + 80000
#     elif beds < 0 and baths > 0 : return (baths * 10000) + 80000
#     elif beds > 0 and baths > 0 : return (beds * 30000) + (baths * 10000) + 80000
#     else : return 80000 - abs((beds-baths)*5000)

#todo: You can also write like this function this is easy way
def get_expected_cost(beds, baths):
    price = 80000 + (beds * 30000) + (baths * 10000)
    return price

#* Call the function and calculate the price of the house
callFunc = get_expected_cost(2,2)
print(callFunc) # Output: 160000