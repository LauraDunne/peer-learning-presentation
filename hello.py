import leap_year

print("Hello User, you are looking well today!")
print("Would you like to:")
print("1: Check if a year is a leap year?")
print("2: Print the prime numbers up to a given integer?")
ans = int(input("Please enter 1 or 2 :"))
if ans == 1:
    leap_year.leap_year_function()
