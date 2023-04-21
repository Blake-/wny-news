from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import ephem
import datetime

#def index(request):
jamestown = 'https://www.post-journal.com/'
response = requests.get(jamestown)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
jamestown_news = []
articles = soup.find_all('article')
for article in articles[:3]:
 title = article.find('h1').text
 url = article.find('a').get('href')
 j_context = {
  'title': title,
  'url': url,
 }
 jamestown_news.append(j_context)

#def index(request):
buffalo = 'https://www.buffalonews.com/'
response = requests.get(buffalo)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
buffalo_news = []
articles = soup.find_all('h3', class_='tnt-headline')
for article in articles[:3]:
 title = article.find('a').text.strip().replace("\n", "")
 url = article.find('a').get('href')
 b_context = {
  'title': title,
  'url': url,
 }
 buffalo_news.append(b_context)

#def index(request):
niagara = 'https://www.niagara-gazette.com/'
response = requests.get(niagara)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
ni_news = []
articles = soup.find_all('h3', class_='tnt-headline')
for article in articles[:3]:
 title = article.find('a').text.strip().replace("\n", "")
 url = article.find('a').get('href')
# print(url)
# print(title)
 n_context = {
  'title': title,
  'url': url,
 }
 ni_news.append(n_context)

wgrz = 'https://www.wgrz.com/news'
response = requests.get(wgrz)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
wgrz_news = []
#articles = soup.find_all('div', class_='headline-list')
articles = soup.find_all('li', class_='headline-list__item')
for article in articles[:3]:
 title = article.find('a').text
 url = article.find('a').get('href')
 grztv_context = {
  'title': title,
  'url': url,
 }
 wgrz_news.append(grztv_context)

olean = 'https://www.oleantimesherald.com/'
response = requests.get(olean)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
olean_news = []
articles = soup.find_all('h3', class_='tnt-headline headline')
for article in articles[:3]:
 title = article.find('a').get('aria-label')
 url = article.find('a').get('href')
 o_context = {
  'title': title,
  'url': url,
 }
 olean_news.append(o_context)

batavia = 'https://www.thedailynewsonline.com/'
response = requests.get(batavia)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
batavia_news = []
articles = soup.find_all('h4', class_='tnt-headline')
for article in articles[:3]:
 title = article.find('a').get('aria-label')
 url = article.find('a').get('href')
 print(title)
 print(url)
 batavia_context = {
  'title': title,
  'url': url,
 }
 batavia_news.append(batavia_context)


###############################
'''
import datetime
import pytz
from astral.sun import sun
from astral import LocationInfo

# Set the location of Buffalo, New York
city = LocationInfo("Buffalo", "New York", "US", 42.8864, -78.8784)

# Create a `Sun` object for the current date and location
s = sun(city.observer, date=datetime.date.today())

# Get the sunrise and sunset times
sunrise = s['sunrise'].astimezone(pytz.timezone('America/New_York'))
sunset = s['sunset'].astimezone(pytz.timezone('America/New_York'))

# Format the times using strftime()
print("Sunrise:", sunrise.strftime('%I:%M:%S %p'))
print("Sunset:", sunset.strftime('%I:%M:%S %p'))
'''
#######################################

def index(request):
 return render(request, 'index.html', {'jamestown_news':jamestown_news, 'buffalo_news': buffalo_news, 'ni_news': ni_news, 'wgrz_news': wgrz_news, 'olean_news': olean_news, 'batavia_news': batavia_news})
