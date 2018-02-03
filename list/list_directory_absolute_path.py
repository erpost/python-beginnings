import os

DIR = '/tmp/files/'

for dirpath, dirnames, filenames in os.walk(DIR):
    for file in filenames:
        print(os.path.abspath(file))