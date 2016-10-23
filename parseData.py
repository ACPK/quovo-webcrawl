import requests
from bs4 import BeautifulSoup as Soup
from collections import OrderedDict
import csv
import sys, traceback
import utility as u

def generateCSVFromURL(url):
  try:    
    reportSoup = u.getSoupFromURL(url)
    fields, rowDataDict, fileName = parseSoupForRelevantData(reportSoup)
    writeCSV(fields, rowDataDict, fileName)
  except:
    traceback.print_exc(file=sys.stdout)

def parseSoupForRelevantData(soup):
  # the 'rows' of the table are made up of <infotable> tags which do not describe any other elements in the xml
  # each row will have the same fields
  rows = soup.find_all('infotable')
  fields = gatherColumnNames(rows[0])
  # this is a list of each row of data represented as a dictionary of field: rowFieldValue 
  rowDataDict = [parseSingleRow(row, fields) for row in rows]
  fileName = generateCSVName(soup)
  return fields, rowDataDict, fileName

def generateCSV(soup):
  # the 'rows' of the table are made up of <infotable> tags which do not describe any other elements in the xml
  # each row will have the same fields
  rows = soup.find_all('infotable')
  fields = gatherColumnNames(rows[0])
  # this is a list of each row of data represented as a dictionary of field: rowFieldValue 
  rowDataDict = [parseSingleRow(row, fields) for row in rows]
  fileName = generateCSVName(soup)
  # write this data to csv file
  writeCSV(fileName, fields, rowDataDict)
  
def gatherColumnNames(row):
  children = row.findChildren()
  # we want a list without the divs that wrap nested columns  
  columns = map(extractNestedColumns, children)
  cleanColumns = [x for x in columns if x != None]
  return cleanColumns

def hasNoNestedColumns(column):
  return len(column.findChildren()) == 0

def extractNestedColumns(column):
  if hasNoNestedColumns(column):
    return column.name
  
def parseSingleRow(row, fields):
  output = OrderedDict()  
  for column in fields:
    output[column] = row.find(column).text
  return output

# We will generate a name using the name of the fund, the CIK ID, the date, the form type
def generateCSVName(soup):
  # data we care about
  fundName = soup.find('filingmanager').find('name').text.replace(" ","")
  cik = soup.find('cik').text
  date = soup.find('periodofreport').text
  formType = soup.find('submissiontype').text

  # an informative csv name  
  csvName = '-'.join([fundName, cik, date, formType]) + '.csv'
  return csvName

def writeCSV(fields, dataDict, docName):
  with open(docName , 'w') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fields)
    writer.writeheader()
    writer.writerows(dataDict)
