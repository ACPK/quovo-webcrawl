from utility import getSoupFromURL


class EdgarFiling:
  def __init__(self, cik, form):
    self.cik = cik
    self.form = form
    self.mostRecentAccession = self._getAccessionNumber()
    self.filingURL = self._getFilingURL()

  # there is a programmatic way to create the url to which we make a request for the txt filing data
  def _getFilingURL(self):
    if self.mostRecentAccession != 'No Reports Available':
      formattedAccession = self._formatAccession()
      formattedCIK = self.cik.lstrip("0").replace('\n', '')
      filingURL = "https://www.sec.gov/Archives/edgar/data/{}/{}/{}.txt".format(formattedCIK, formattedAccession, self.mostRecentAccession)
      return filingURL
    else:
      return 'No Reports Available'

  def _formatAccession(self):
    return self.mostRecentAccession.replace("-", "")

  # Get the accession number of the most recent filing of the relevant form type
  def _getAccessionNumber(self):
    # some companies have not filed that specific form
    try:
      # this url is to a query of all forms of the chosen type, by the chosen CIK
      queryURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&type={}&output=atom".format(self.cik, self.form)
      document = getSoupFromURL(queryURL)
      # they spell 'accession NUMBER' wrong it seems...
      accessionNumber = document.find('accession-nunber').text
      return accessionNumber
    except:
      return 'No Reports Available'
