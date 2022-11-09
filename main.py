#Load in the necessary libaries

import requests
from bs4 import BeautifulSoup as bs

#Load the webpage content

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

# Convert to a beautiful soup object

webpage = bs(r.content)

print(webpage.prettify())

#Exercise 1

#method 1

links = webpage.select("ul.socials a")
realLinks = [link['href'] for link in links]
print (realLinks)

#method 2

links = webpage.select('li.social a')
print (links)

#Exercise 2

import pandas as pd

table = webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
columnNames = [c.string for c in columns]

tableRows = table.find("tbody").findAll("tr")
l = []
for tr in tableRows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

df = pd.DataFrame(1, columns=columnNames)
df.head()
print(l[0])

#Exercise 3

import re

facts = webpage.select("ul.fun-facts li")
factsWithIs = [facts.find(string=re.compile("is")) for fact in facts]
factsWithIs = [fact.find_parent().get_text() for fact in factsWithIs if fact]
print(factsWithIs)

#Exercise 5

files = webpage.select('div.block a')
relative_files = [f['href'] for f in files]

url = "https://keithgali.github.io/web-scraping/"
for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content)
    secret_world_element = bs_page.find("p", attrs=("id": "secret-word"))
    secret_word = secret_word_element.string
    print(secret_word)

