from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")
#print(soup)

# Retrieve all of the anchor tags
tags = soup('span')

lst = list()

for tag in tags:
        # Look at the parts of a tag
        #    print('TAG:', tag)
        #    print('URL:', tag.get('href', None))
        #    print('Contents:', tag.contents[0])
        #    print('Attrs:', tag.attrs)
    lst.append(int(tag.contents[0]))
print(sum(lst))
