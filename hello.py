import leap_year
import primes
import pandas

print("Hello User, you are looking well today!")
print("Would you like to:")
print("1: Check if a year is a leap year?")
print("2: Print the prime numbers up to a given integer?")
<<<<<<< HEAD
print("3: Print the Fibonaci sequence to a given integer?")
print("4: Get the factorial of something")
ans = int(input("Please enter 1, 2 or 3:"))

while ans != 1 and ans != 2:
    ans = int(input("Please enter 1 or 2:"))
=======
ans = int(input("Please enter 1 or 2 :"))
>>>>>>> parent of 9004857... adding Fibonaci sequence

if ans == 1:
    leap_year.leap_year_function()

if ans == 2:
    primes.print_primes()
<<<<<<< HEAD

if ans == 3:
    fib.print_sequence()

if ans == 4:
    
=======
>>>>>>> parent of 9004857... adding Fibonaci sequence
