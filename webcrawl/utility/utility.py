import requests
from bs4 import BeautifulSoup as Soup

def getSoupFromURL(url):
  html = requests.get(url).content
  document = Soup(html, 'html.parser')
  return document
