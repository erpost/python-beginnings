import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print(local_time)

# print all timezones
for tz in pytz.all_timezones:
    print(tz)

# print countries with abbreviations
for c in sorted(pytz.country_names):
    print(c + ': ' + pytz.country_names[c])

# print countries, abbreviations and associated timezones
for c in sorted(pytz.country_names):
    print('{}: {}: {}'.format(c, pytz.country_names[c], pytz.country_timezones.get(c)))
