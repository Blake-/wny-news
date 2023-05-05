####
## This code is A MESS don't use it for anything!
####

import requests
from bs4 import BeautifulSoup
import feedparser
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import ephem
import datetime
import logging


#def index(request):
jamestown = 'https://www.post-journal.com/'
response = requests.get(jamestown)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
jamestown_news = []
articles = soup.find_all('article')
for article in articles[:6]:
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
for article in articles[:6]:
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
for article in articles[:6]:
 title = article.find('a').text.strip().replace("\n", "")
 url = article.find('a').get('href')
# print(url)
# print(title)
 n_context = {
  'title': title,
  'url': url,
 }
 ni_news.append(n_context)


url = "https://www.wkbw.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

article_blocks = soup.find_all("div", class_="List-items-row-item")
wkbw_news = []
for article in article_blocks[:6]:
    title = article.find("h3", class_="ListItem-title").text.strip()
    url = article.find("a")["href"]
    print(title)
    print(url)
    kb_context = {
     'title': title,
     'url': url,
    }
    wkbw_news.append(kb_context)



wgrz = 'https://www.wgrz.com/news'
response = requests.get(wgrz)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
wgrz_news = []
#articles = soup.find_all('div', class_='headline-list')
articles = soup.find_all('li', class_='headline-list__item')
for article in articles[:6]:
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
for article in articles[:6]:
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
for article in articles[:6]:
 title = article.find('a').get('aria-label')
 url = article.find('a').get('href')
 batavia_context = {
  'title': title,
  'url': url,
 }
 batavia_news.append(batavia_context)

#rochester = 'https://www.democratandchronicle.com/'
#response = requests.get(rochester)
#html_content = response.content
#soup = BeautifulSoup(html_content, 'html.parser')
#rochester_news = []
#articles = soup.find_all('div', class_='gnt_m gnt_m_lb')
#for article in articles[:6]:
# title = article.find('a').text
# url = article.find('a').get('href')
# rochester_context = {
#  'title': title,
#  'url': url,
# }
# rochester_news.append(rochester_context)


#url = "https://www.nytimes.com/"
#response = requests.get(url)
#soup = BeautifulSoup(response.content, "html.parser")
#nytimes_news = []
#story_wrappers = soup.find_all("section", {"class": "story-wrapper"})
#for story_wrapper in story_wrappers[:6]:
#    headline_tag = story_wrapper.find("h3", {"class": "indicate-hover"})
#    if headline_tag is not None:
#        headline = headline_tag.text.strip()
#        article_link = story_wrapper.find("a")
#        if article_link is not None:
#            article_link = article_link["href"]
#            nytimes_context = {
#             'headline': headline,
#             'article_link': article_link,
#            }
#            print(headline)
#            print(article_link)
#            nytimes_news.append(nytimes_context)



import requests
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/product.php?site=BUF&issuedby=BUF&product=AFD&format=TXT&version=1&glossary=0&highlight=off'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

pre_elements = soup.find_all('pre')
for pre_element in pre_elements:
    if '.SYNOPSIS...' in pre_element.text:
        start_index = pre_element.text.index('.SYNOPSIS...') + len('.SYNOPSIS...')
        end_index = pre_element.text.index('&&')
        result = pre_element.text[start_index:end_index].strip()
        result = result.replace('-- Changed Discussion --', '')
        result = result.replace('-- End Changed Discussion --', '')
        weather = result
#        print(result.strip())
        break
else:
    print('No weather found.')

reddit = "https://www.reddit.com/r/Buffalo/rising/.rss"
feed = feedparser.parse(reddit)
reddit_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    reddit_context = {
     'title': title,
     'url': url,
    }
    reddit_news.append(reddit_context)

bizjournals = "http://feeds.bizjournals.com/bizj_buffalo"
feed = feedparser.parse(bizjournals)
biz_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    biz_context = {
     'title': title,
     'url': url,
    }
    biz_news.append(biz_context)

rochester = "http://rssfeeds.democratandchronicle.com/Democratandchronicle/BreakingNewsAndTopStories"
feed = feedparser.parse(rochester)
rochester_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
#    print(title)
    rochester_context = {
     'title': title,
     'url': url,
    }
    rochester_news.append(rochester_context)

nytimes = "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/nyregion/rss.xml"
feed = feedparser.parse(nytimes)
nytimes_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
#    print(title)
    nytimes_context = {
     'title': title,
     'url': url,
    }
    nytimes_news.append(nytimes_context)

toronto = "http://www.thestar.com/content/thestar/feed.RSSManagerServlet.articlestopstories.rss"
feed = feedparser.parse(toronto)
toronto_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
#    print(title)
    toronto_context = {
     'title': title,
     'url': url,
    }
    toronto_news.append(toronto_context)

history = "http://news.bbc.co.uk/rss/on_this_day/front_page/rss.xml"
feed = feedparser.parse(history)
history_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    history_context = {
     'title': title,
     'url': url,
    }
    history_news.append(history_context)

axios = "https://api.axios.com/feed/"
feed = feedparser.parse(axios)
axios_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    axios_context = {
     'title': title,
     'url': url,
    }
    axios_news.append(axios_context)


theverge = "https://www.theverge.com/rss/index.xml"
feed = feedparser.parse(theverge)
theverge_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    theverge_context = {
     'title': title,
     'url': url,
    }
    theverge_news.append(theverge_context)

buffalorising = "https://www.buffalorising.com/feed/"
feed = feedparser.parse(buffalorising)
buffalorising_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    buffalorising_context = {
     'title': title,
     'url': url,
    }
    buffalorising_news.append(buffalorising_context)

artvoice = "https://artvoice.com/feed/"
feed = feedparser.parse(artvoice)
artvoice_news = []
for entry in feed.entries[:6]:
    title = entry.title
#    print(title)
    url = entry.link
    artvoice_context = {
     'title': title,
     'url': url,
    }
    artvoice_news.append(artvoice_context)


wbfo = "https://www.wbfo.org/tags/regional-news.rss"
feed = feedparser.parse(wbfo)
wbfo_news = []
for entry in feed.entries[:6]:
    title = entry.title
#    print(title)
    url = entry.link
    wbfo_context = {
     'title': title,
     'url': url,
    }
    wbfo_news.append(wbfo_context)


wivb = "https://www.wivb.com/feed/"
feed = feedparser.parse(wivb)
wivb_news = []
for entry in feed.entries[:6]:
    title = entry.title
#    print(title)
    url = entry.link
    wivb_context = {
     'title': title,
     'url': url,
    }
    wivb_news.append(wivb_context)

spectrum = "https://spectrumlocalnews.com/services/contentfeed.nys%7cbuffalo%7cnews.landing.rss"
feed = feedparser.parse(spectrum)
spectrum_news = []
for entry in feed.entries[:6]:
    title = entry.title
    print(title)
    url = entry.link
    spectrum_context = {
     'title': title,
     'url': url,
    }
    spectrum_news.append(spectrum_context)


## move everything fetching RSS?

url = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258'
response = requests.get(url)
feed = feedparser.parse(response.content)
cnbc_news = []
for entry in feed.entries[:6]:
    title = entry.title
    url = entry.link
    # Fetch the full article page to extract additional information
    article_response = requests.get(url)
    article_soup = BeautifulSoup(article_response.content, "html.parser")
    summary = article_soup.find('div', {'class': 'group'}).text.strip()

    cnbc_context = {
        'title': title,
        'url': url,
    }
    cnbc_news.append(cnbc_context)






###############################

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

srise = sunrise.strftime('%-I:%M')
sset = sunset.strftime('%-I:%M')

#######################################


def index(request):
# return render(request, 'index.html', {'biz_news':biz_news})
 return render(request, 'index.html', {'spectrum_news':spectrum_news, 'wkbw_news':wkbw_news, 'wivb_news':wivb_news, 'wbfo_news':wbfo_news, 'artvoice_news':artvoice_news, 'buffalorising_news':buffalorising_news, 'theverge_news':theverge_news, 'axios_news':axios_news, 'history_news':history_news, 'toronto_news':toronto_news, 'cnbc_news':cnbc_news, 'biz_news':biz_news, 'reddit_news':reddit_news, 'weather':weather, 'sunrise':srise, 'sunset':sset, 'jamestown_news':jamestown_news, 'buffalo_news': buffalo_news, 'ni_news': ni_news, 'wgrz_news': wgrz_news, 'olean_news': olean_news, 'batavia_news': batavia_news, 'rochester_news':rochester_news, 'nytimes_news': nytimes_news})



