import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location: ')
if len(address) < 1: address = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()

print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
lst2 = []

for item in lst:
    lst2.append(int(item.find('count').text))
print('Count', len(lst2))
print('Sum:', sum(lst2))
