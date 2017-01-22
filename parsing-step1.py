# Parsing congress.gov/members/

import requests
from html.parser import HTMLParser
from lxml import html
from lxml.html import fromstring

# FIRST: Get Senators and Reps's names, party, state, district and their websites.

# create dictionary
takeadict = []

# get info from website
page = requests.get('https://www.congress.gov/members?pageSize=250&q={"congress":"115"}')
tree = html.fromstring(page.content)

# get senator urls
hrefs = tree.xpath('//select[@id="members-senators"]/option/@value')
del hrefs[0]
print(len(hrefs))

# get representative urls
representativehrefs = tree.xpath('//select[@id="members-representatives"]/option/@value')
del representativehrefs[0]
print(len(representativehrefs))

# put senators in dictionary
for i in range(441):
    hrefs.append( representativehrefs[ i ] )
