import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"
r_iban = requests.get(url)

html_iban = r_iban.text

soup = BeautifulSoup(html_iban, 'html.parser')
print(soup)