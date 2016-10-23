from generatePaths import EdgarFiling

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
    



  def _generateAllURLs(self):
    def _getFilingURL(cik, form):
      decoded_string = bytes(cik, "utf-8").decode("unicode_escape")      
      currentFiling = EdgarFiling(cik, form)
      filingURL = currentFiling.filingURL
      return filingURL

    with open(self.inputFile, 'r') as myFile:
      allTickers = myFile.readlines()
      self.reportURLs = [_getFilingURL(cik, '13F-HR') for cik in allTickers]
