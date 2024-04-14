# Calculate the Phone Internet Bill

#* You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + (gb - 15) * 100
    return bill

# Test The Function
print(get_phone_bill(5))