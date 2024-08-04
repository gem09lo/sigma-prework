#L3 Challenge 3 Task 1: Age Calculator
#python age.py

from datetime import datetime
from datetime import date
from datetime import timedelta

"""CURRENT DATE"""
current_date = date.today().strftime("%d-%m-%Y")

"""INPUT DATE"""
#my_date = '2011-11-04'
#my_date = date.fromisoformat(my_date).strftime("%d-%m-%Y")
#print(my_date)

def my_date(input_date):
    input_date = date.fromisoformat(input_date).strftime("%d-%m-%Y")
    return input_date
given_date = my_date("2014-11-04")


"""CALCULATE AGE"""
def calculate_age():
   date_1 = datetime.strptime(current_date, '%d-%m-%Y').date()
   date_2 = datetime.strptime(given_date, '%d-%m-%Y').date()
   delta = date_1 - date_2
   age_years = delta.days//365
   return ("Today's date: {} \nGiven date: {} \nAge: {}".format(current_date, given_date, age_years))

print(calculate_age())

