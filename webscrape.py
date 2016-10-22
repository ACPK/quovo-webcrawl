import requests
from bs4 import BeautifulSoup as Soup

url = 'https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/0001104659-16-139781.txt'

def getSoupFromURL(url):
  print('getting url...')  
  html = requests.get(url).content
  document = Soup(html, 'html.parser')
  return document

def generateCSV(soup):
  print('generatingCSV...\n')
  gatherColumnNames()

def gatherColumnNames():
  print('gathering column names')






















def main():
  filing = getSoupFromURL(url)
  csv = generateCSV(filing)

main()
