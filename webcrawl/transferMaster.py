from utility.generatePaths import EdgarFiling
import utility.parseData as pd

class transferProcess:
  def __init__(self, inputFile, formType):
    self.inputFile = inputFile
    self.formType = formType
    self.reportURLs = []
  
  def run(self):
    # First step, get the urls for the txt filing for each id in the input file
    # After this step, everything in ReportURLs will either be a valid url to a filing,
    # or 'No reports available'
    self._generateAllURLs()
    # for every valid url (i.e, the cik and form combo exists), parse that data into csv
    self._generateAllCSVs()

  def _getFilingURL(self, cik, form):
    decoded_string = bytes(cik, "utf-8").decode("unicode_escape")      
    currentFiling = EdgarFiling(cik, form)
    filingURL = currentFiling.filingURL
    return filingURL

  def _generateAllURLs(self):
    with open(self.inputFile, 'r') as myFile:
      allTickers = myFile.readlines()
      self.reportURLs = [self._getFilingURL(cik, '13F-HR') for cik in allTickers]

  def _generateAllCSVs(self):
    for reportURL in self.reportURLs:
      if reportURL != 'No Reports Available':
        pd.generateCSVFromURL(reportURL)
