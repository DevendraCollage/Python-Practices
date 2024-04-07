# TODO: Calculate the number of seconds in 1 years

# Create variable and store the default value
num_years = 1;
# days_per_year = 365.25; This is for leap year
days_per_year = 365; # This is for not leap year
hours_per_day = 24;
mins_per_hour = 60;
second_per_min = 60;

# Calculate the number of seconds in 1 years
total_secs = second_per_min * mins_per_hour * hours_per_day * days_per_year * num_years;
print(total_secs); # Output: 31536000.0