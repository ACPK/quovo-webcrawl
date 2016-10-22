import requests
from bs4 import BeautifulSoup as Soup

url = 'https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/0001104659-16-139781.txt'

def getSoupFromURL(url):
  html = requests.get(url).content
  document = Soup(html, 'html.parser')
  return document

def generateCSV(soup):
  # the 'rows' of the table are made up of <infotable> tags which do not describe any other elements in the xml
  # each row will have the same fields
  rows = soup.find_all('infotable')
  fields = gatherColumnNames(rows[0])

def hasNoNestedColumns(column):
  return len(column.findChildren()) == 0

def extractNestedColumns(child):
  if hasNoNestedColumns(child):
    if child is None:
      return 0
    else:
      return child

def gatherColumnNames(row):
  children = row.findChildren()
  # we want a list without the divs that wrap nested columns  
  columns = map(extractNestedColumns, children)
  cleanColumns = [x for x in columns if x != None]
  return cleanColumns

def main():
  filing = getSoupFromURL(url)
  csv = generateCSV(filing)

main()
