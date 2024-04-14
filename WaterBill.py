# Return a Water Bill on the basis of the wat usage by customer

#* Water Agency Uses This Pricing Structure:
#  Tier	       Amount in gallons	  Price per 1000 gallons
# Tier-1	      0 - 8,000	                  $5
# Tier-2	      8,001 - 22,000	              $6
# Tier-3	      22,001 - 30,000	          $7
# Tier-4	      30,001+	                  $10

def get_water_bill(num_gallon):
    bill = 0
    if num_gallon>=0 and num_gallon<=8000:
        bill = 5
    elif num_gallon>=8001 and num_gallon<=22000:
        bill = 6
    elif num_gallon>=22001 and num_gallon<=30000:
        bill = 7
    else:
        bill = 10

    total_bill = (num_gallon / 1000) * bill # Calculate the total bill of the water                        
    return total_bill

# Test The Function
print(get_water_bill(4000)) # Output: 20        