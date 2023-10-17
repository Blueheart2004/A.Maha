LO

input_year=int(input("enter a year:"))

2 def is leap(year):

3 v

if (year% 400 ==0) or (year % 4==0 and year % 100 !=0):

45 4

return True

5

return False

7

if is_leap(input_year): print("it is a leap year")

8

9v else:

10

print("it is not a leap year")