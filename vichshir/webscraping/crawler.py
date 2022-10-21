from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
import urllib.request
import re


def tag_visible(element):
  if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
      return False
  if isinstance(element, Comment):
      return False
  return True


def website_link_valid(url):
  return 'http://' + url if ('http://' not in url) and ('https://' not in url) else url


def text_from_html(body):
  soup = BeautifulSoup(body, 'html.parser')
  texts = soup.findAll(text=True)
  visible_texts = filter(tag_visible, texts)  
  txt = u" ".join(t.strip() for t in visible_texts)
  return re.sub(r'\W+', ' ', txt)


def scrap(url):
  try:
    url = website_link_valid(url)
    req = Request(
        url=url, 
        headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
    )
    html = urlopen(req).read()
    return text_from_html(html)
  except:
    return None