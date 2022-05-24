import requests
from bs4 import BeautifulSoup


r_iban = requests.get("https://www.iban.com/currency-codes")

html_iban = r_iban.text

soup = BeautifulSoup(html_iban, 'html.parser')
rows = soup.find_all('tr')

currencies = []
id = 0

for row in rows:
    id += 1
    contents = row.contents
    
    currency = {
        "id": id,
        "name": contents[1].string,
        "coin": contents[3].string
    }

    currencies.append(currency)
    print(f"#{currency['id']} {currency['name']}")


def menu():
    try:
        country_code = int(input("Choose a country code #: "))

        if country_code > len(currencies):
            print("This number is bigger than the list")
            menu()
        else:
            country = currencies[country_code]
            print(f"(x) {country['name']}")
            
    
    except ValueError as err:
        print("Please select a number.", err)

menu()