def convert_currency(amount, from_currency, to_currency, rates):
    try:
        return amount * (rates[to_currency] / rates[from_currency])
    except KeyError:
        raise ValueError(f"Neplatná měna: {from_currency} nebo {to_currency}")
amount = float(input("Zadejte množství: "))
from_currency = input("Z jaké měny: ")
to_currency = input("Do jaké měny: ")
rates = {'Kč': 1, 'euro': 0.041, 'dolar': 0.045}
print(f"Výsledek: {convert_currency(amount, from_currency, to_currency, rates)} {to_currency}")