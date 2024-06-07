def leap_year_2(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Enter the year :"))
if leap_year_2(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

