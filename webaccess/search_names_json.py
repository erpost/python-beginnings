import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
if len(address) < 1: address = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print('User count:', len(js['comments']))

# print all names in json array
#for i in range(len(js['comments'])):
#    print(js['comments'][i]['name'])

count_list = list()

#append all counts in json array
for i in range(len(js['comments'])):
    # print(i)
    count_list.append(js['comments'][i]['count'])
print('Sum:', sum(count_list))
