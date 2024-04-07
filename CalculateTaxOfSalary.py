# Write the function to calculate the tax you have to pay on your salary

pay_partime = 0; #* This variables have an global scope and can access from outside the function and from anywhere
def get_pay(hours):
    pay_pretax = hours * 15 #* And this variable scope is to the function you cannot access the variables outside of the function this have a local scope to function
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

print(get_pay(50)) # Output: 660.0 $/month This the value you get after paying the tax you have to pay on your salary