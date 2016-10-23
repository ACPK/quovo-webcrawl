from generatePaths import EdgarFiling

class transferProcess:
  def __init__(self, inputFile):
    self.inputFile = inputFile
    self.reportURLs = []
  
  def run(self):
    print('hiya!')
    # First step, get the 










  def _generateURLs(self):    
    def _getFilingURL(cik, form):
      decoded_string = bytes(cik, "utf-8").decode("unicode_escape")      
      currentFiling = EdgarFiling(cik, form)
      filingURL = currentFiling.filingURL
      return filingURL

    with open(self.inputFile, 'r') as myFile:
      allTickers = myFile.readlines()
      self.reportURLs = [_getFilingURL(cik, '13F-HR') for cik in allTickers]
