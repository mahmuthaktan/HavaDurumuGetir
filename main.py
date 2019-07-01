import requests
from bs4 import BeautifulSoup


link  = 'https://www.timeanddate.com/weather/@738329/historic?month=10&year=2018'

def amazon(url):
    sourcecode = requests.get(url)
    sourcecode_text = sourcecode.text
    soup = BeautifulSoup(sourcecode_text, "html.parser")
    # add "html.parser" as second arg , so you not get a warning .
    # use soup.find_all for new code , also soup.findAll should work
    for link in soup.find_all('a', {'class': 'a-link-normal aok-block a-text-normal'}):
        href = link.get('href')
        print(href)

amazon(link)
