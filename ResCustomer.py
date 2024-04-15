# The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days). Fill in values for each of the following:

#? 1. avg_first_seven - average number of customers who visited in the first seven days
#? 2. avg_last_seven - average number of customers who visited in the last seven days
#? 3. max_month - number of customers on the day that got the most customers in the last month
#? 4. min_month - number of customers on the day that got the least customers in the last month


num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

print(sum(num_customers[0:7])/7) # Output: 150.86

print(sum(num_customers[len(num_customers)-7:len(num_customers)])/7) # Output: 157.0
print(max(num_customers[:len(num_customers)])) # Output: 174
print(min(num_customers[:len(num_customers)])) # Output: 126