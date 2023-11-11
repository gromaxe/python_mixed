import requests


def get_exchange_rates(base_currency='EUR'):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching the exchange rates.")
        return None

    return response.json()


def list_available_currencies():
    data = get_exchange_rates()
    if data:
        return list(data['rates'].keys())
    return []


def convert_currency(amount, base_currency, target_currency):
    data = get_exchange_rates(base_currency)
    if data is None:
        print(f"Conversion rate not available for {base_currency}.")
        return None

    if base_currency != 'EUR' and target_currency != 'EUR':
        rate_to_eur = data['rates'].get('EUR')
        data = get_exchange_rates('EUR')
        rate_from_eur_to_target = data['rates'].get(target_currency)
        rate = rate_to_eur * rate_from_eur_to_target
    else:
        rate = data['rates'].get(target_currency)

    if rate is None:
        print(f"Conversion rate not available for {target_currency}.")
        return None
    return amount * rate


if __name__ == "__main__":
    print("Available currencies:", ", ".join(list_available_currencies()))
    base_currency = input("Enter your base currency (e.g., EUR, USD): ").upper()
    target_currency = input("Enter the target currency (e.g., USD, GBP): ").upper()
    amount = float(input("Enter the amount in your base currency: "))

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is approximately equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed.")
