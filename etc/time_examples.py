import time

print(time.gmtime(0))

print(time.localtime())

print(time.time())

time_here = time.localtime()
print(time_here)
print('Year:', time_here[0], time_here.tm_year)
print('Year:', time_here[1], time_here.tm_mon)
print('Year:', time_here[2], time_here.tm_mday)
