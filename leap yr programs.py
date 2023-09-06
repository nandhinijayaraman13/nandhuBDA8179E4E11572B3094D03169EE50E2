"""
input_year=int(input("enter a year:"))
def is_leap(year):
    if year%400==0 or year%4==0:
      return True
if is_leap(input_year):
   print("it is leap yr")   
else:
    print("it is not leap yr")
"""
import calendar
input_year=int(input("enter a year:"))
if calendar.isleap(input_year):
    print("it is leap year")
else:
    print("it is not leap yr")
      
