year=int(input("Enter the year:"))
if year%400==0 or year%100!=0 and year%4==0:
    print("Year is a leap year")
else:
     print("Year is not a leap year")