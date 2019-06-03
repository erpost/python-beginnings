import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4455</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone Type:', tree.find('phone').get('type'))
print('Name:', tree.find('phone').text)
print('Email Hidden:', tree.find('email').get('hide'))
