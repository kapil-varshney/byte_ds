"""
Part 2

The datetime module provides data and time objects and a rich set of methods and operators. Read the documentation here. Submit the following in a file named date.py.

1. Use the datetime module to write a program that gets the current date and prints the day of the week.
2. Write a program that takes a birthday as input and prints the user age and the number of days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other. Thats their Double Day. Write a program that takes two birthdays and computes their Double Day.
4. For a little more challenge, write the more general version that computes the day when one person is n times older than the other.
"""

import datetime as dt
# import dateutil

# Function to return the day of the week today (Monday = Day 1)
def day_of_week():

	today = dt.date.today()
	return (today.isoweekday())


def next_bday(birthdate):
	
	dob = dt.datetime.strptime(birthdate, '%Y-%m-%d')
	today = dt.datetime.today()
	print (age_in_days(today, dob))
	

	if ((dob.month, dob.day) < (today.month, dob.day)):
		next_bday = dob.replace(year = today.year +1)
	else:
		next_bday = dob.replace(year = today.year)

	time_to_bday = next_bday - today
	return (time_to_bday)
	

def age_in_days(today, dob) :
	return (today - dob)

"""
def age_in_years(today, dob):

	print today, dob
	age_in_years = dateutil.relativedelta.relativedelta(today, dob)
	print (age_in_years)
	#return age_in_years
"""

def double_day(birthdate1, birthdate2):
	
	dob1 = dt.datetime.strptime(birthdate1,'%Y-%m-%d')
	dob2 = dt.datetime.strptime(birthdate2,'%Y-%m-%d')

	if (dob1 < dob2):
		dd = dob2 + (dob2 - dob1)
	else:
		dd = dob1 + (dob1 - dob2)

	return (dt.date(dd.year, dd.month, dd.day))

def strip_time(d):
	return (dt.date(d.year, d.month, d.day))

def n_day(birthdate1, birthdate2, n):
	dob1 = strip_time(dt.datetime.strptime(birthdate1,'%Y-%m-%d'))
	dob2 = strip_time(dt.datetime.strptime(birthdate2,'%Y-%m-%d'))
	today = dt.date.today()

	age1 = age_in_days(today, dob1)
	age2 = age_in_days(today, dob2)

	if (age1 < age2) :
		age1, age2 = age2, age1

	n_day = today + (age1 - n*age2)/(n-1)

	return (n_day)


#print (next_bday('1990-04-14'))
#print (double_day('2000-10-04','1990-10-14'))
#print (n_day('1990-10-14','2000-10-04', 7))