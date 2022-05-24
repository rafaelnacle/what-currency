import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


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
        "coin": contents[5].string
    }

    currencies.append(currency)
    print(f"#{currency['id']} {currency['name']}")


base_wise_url = 'https://wise.com/gb/currency-converter/'
def exchange(currency1, currency2, amount):
    try:
        total = 0
        r_wise = requests.get(
            f"{base_wise_url}{currency1}-to-{currency2}-rate?amount={amount}",
            headers={
                "user-agent":
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
            })
        html_wise = r_wise.text
        soup = BeautifulSoup(html_wise, 'html.parser')

        h3 = soup.find('h3', class_="cc__source-to-target")
        spans = h3.find_all('span')
        
        value2 = spans[2].text.strip()

        total = float(amount) * float(value2)

        formated_currency1 = format_currency(amount, currency1.upper())
        formated_currency2 = format_currency(total, currency2.upper())

        return f"{formated_currency1} is equal to {formated_currency2}"
        
    except AttributeError as err:
        print(err)


def menu():
    is_selecting = True
    while is_selecting:
        try:
            first_country_code = int(input("Choose a country code #: "))
    
            if first_country_code > len(currencies):
                print("This number is bigger than the list")
                menu()
            else:
                first_country = currencies[first_country_code]
                print(f"(x) {first_country['name']}")
    
            second_country_code = int(input("Wich country you want to exchange? "))
            if second_country_code > len(currencies):
                print("This number is bigger than the list")
                menu()
            else:
                second_country = currencies[second_country_code]
                print(f"(x) {second_country['name']}")
    
            amount = float(
                input(
                    f"How much {first_country['coin']} you want to exchange to {second_country['coin']}? "
                ))
            is_selecting = False
    
            print(exchange(first_country['coin'].lower(), second_country['coin'].lower(), amount))

        except ValueError as err:
        
            print("Please select a number.", err)

menu()
