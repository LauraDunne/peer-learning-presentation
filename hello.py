import leap_year
import primes
import fib 

print("Hello User, you are looking well today!")
print("Would you like to:")
print("1: Check if a year is a leap year?")
print("2: Print the prime numbers up to a given integer?")
print("3: Print the Fibonaci sequence to a given integer?")
ans = int(input("Please enter 1, 2 or 3:"))

if ans == 1:
    leap_year.leap_year_function()

if ans == 2:
    primes.print_primes()

if ans == 3:
    fib.print_sequence()
