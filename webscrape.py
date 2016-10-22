import requests

print('webscrapping...')

url = 'https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/0001104659-16-139781.txt'

response = requests.get(url)
html = response.content

print(html)

