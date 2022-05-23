import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"
r_iban = requests.get(url)

html_iban = r_iban.text

soup = BeautifulSoup(html_iban, 'html.parser')
rows = soup.find_all('tr')

currencies = []
id = 0

for row in rows[1:]:
    id += 1
    contents = row.contents
    
    currency = {
        "id": id,
        "country": contents[1].string,
        "coin": contents[3].string
    }

    currencies.append(currency)
    print(f"#{currency['id']} {currency['country']}")

try:
    code = int(input("Choose a country code to check its coin #: "))

    for currency in currencies:
        if code == currency['id']:
            print(f"You chose {currency['country']}")
            print(f"The coin code is: {currency['coin']}")

except ValueError as err:
    print("Please select a number.", err)
