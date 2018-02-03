from datetime import datetime
###################################
# stores current date in variable 'now'
now = datetime.now()

# stores current year/month/day variables using 'now' variable
current_year = now.year
current_month = now.month
current_day = now.day

#prints each variable
print(now)
print(current_year)
print(current_month)
print(current_day)

###################################
#prints the current time directly
print(datetime.now())

#prints the current year
print(datetime.now().year)

#prints the current month
print(datetime.now().month)

#prints the current day
print(datetime.now().day)

###################################
# additional way to print year/month/day
import time

year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')

print(year)
print(month)
print(day)

###################################

