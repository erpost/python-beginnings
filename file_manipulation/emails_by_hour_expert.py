import re
import collections
import time

def parse_distribution():

    # pre-compile regex for speed!
    EMAIL = re.compile(r'^From (\S*) (.*)')

    # Counter class to tally up the emails received each hour
    time_dist = collections.Counter()

    # use a context manager to make sure the file is closed properly
    with open('mbox-short.txt') as f:

        for line in f.readlines():
            m = EMAIL.match(line)
            if m:
                t = m.group(2)
                time_obj = time.strptime(t) # way easier than parsing!
                time_dist[time_obj.tm_hour] += 1

    return sorted(time_dist.items())

time_dist = parse_distribution()

for k, v in time_dist:
    print(k, v)