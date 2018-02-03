from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

i = 8

while i != 0:
    print('Retrieving:', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))
    url = lst[17]
    i -= 1
