import time
from time import perf_counter as my_timer
import random

input('Press Enter to start')

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press Enter to stop')

end_time = my_timer()

print('Started at ' + time.strftime('%X', time.localtime(start_time)))
print('Ended at ' + time.strftime('%X', time.localtime(end_time)))

print('Your reaction time was {} seconds'.format(end_time - start_time))




























