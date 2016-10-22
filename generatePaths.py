import requests
from bs4 import BeautifulSoup as Soup

cik = '0001166559'

def getSoupFromURL(url):
  html = requests.get(url).content
  document = Soup(html, 'html.parser')
  return document

class EdgarFiling:
  def __init__(self, cik, form):
    self.cik = cik
    self.form = form
    self.rawAccession = self.getAccessionNumber()

  def getURL(self):
    formattedAccession = self.formatAccession()
    url = "https://www.sec.gov/Archives/edgar/data/{}/{}/{}.txt".format(self.cik.lstrip("0"), formattedAccession, self.rawAccession)
    print(url)

  def formatAccession(self):
    return self.rawAccession.replace("-", "")

  # Get the accession number of the most recent filing of 
  def getAccessionNumber(self):    
    url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&type={}&output=atom".format(self.cik, self.form)
    document = getSoupFromURL(url)
    # they spell 'accession NUMBER' wrong it seems...
    accessionNumber = document.find('accession-nunber').text
    return accessionNumber


# https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/0001104659-16-139781.txt

def main():
  filing = EdgarFiling(cik, '13F-HR')
  filing.getURL()

main()
