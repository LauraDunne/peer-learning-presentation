def leap_year_function():
    year = int(input("Please enter year :"))

    if year <= 0:
        print("The year must be expressed in astronomical year numbering!")

    else:
        if year %4 == 0 and year %100!= 0 or year %400 ==0:
            print(str(year)+" " + "is a leap year!")
            
        else: print(str(year) + " " + "is a common year!")


if __name__ == '__main__':
    leap_year_function()