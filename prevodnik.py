def convert_currency(amount, from_currency, to_currency):
    rates = {
        'CZK': {'EUR': 0.04, 'USD': 0.045},
        'EUR': {'CZK': 25, 'USD': 1.12},
        'USD': {'CZK': 22, 'EUR': 0.89}
    }
    try:
        return amount * rates[from_currency][to_currency]
    except KeyError:
        return "špatná jednotka!"

def convert_distance(amount, from_unit, to_unit):
    units = {
        'loket': {'sáh': 0.5, 'píď': 2, 'palec': 24, 'stopa': 2},
        'sáh': {'loket': 2, 'píď': 4, 'palec': 48, 'stopa': 4},
        'píď': {'loket': 0.5, 'sáh': 0.25, 'palec': 12, 'stopa': 1},
        'palec': {'loket': 0.0417, 'sáh': 0.0208, 'píď': 0.0833, 'stopa': 0.0833},
        'stopa': {'loket': 0.5, 'sáh': 0.25, 'píď': 1, 'palec': 12}
    }
    try:
        return amount * units[from_unit][to_unit]
    except KeyError:
        return "špatná jednotka!"

def convert_weight(amount, from_unit, to_unit):
    units = {
        'libra': {'unce': 16, 'kámen': 0.0714, 'gram': 453.592, 'kilogram': 0.453592},
        'unce': {'libra': 0.0625, 'kámen': 0.004464, 'gram': 28.3495, 'kilogram': 0.0283495},
        'kámen': {'libra': 14, 'unce': 224, 'gram': 6350.29, 'kilogram': 6.35029},
        'gram': {'libra': 0.00220462, 'unce': 0.035274, 'kámen': 0.000157473, 'kilogram': 0.001},
        'kilogram': {'libra': 2.20462, 'unce': 35.274, 'kámen': 0.157473, 'gram': 1000}
    }
    try:
        return amount * units[from_unit][to_unit]
    except KeyError:
        return "špatná jednotka!"

def convert_energy(amount, from_unit, to_unit):
    units = {
        'joule': {'calorie': 0.239006, 'electronvolt': 6.242e+18, 'kilowatthodina': 2.77778e-7},
        'calorie': {'joule': 4.184, 'electronvolt': 2.611e+19, 'kilowatthodina': 1.16222e-6},
        'electronvolt': {'joule': 1.60218e-19, 'calorie': 3.829e-20, 'kilowatthodina': 4.4505e-26},
        'kilowatthodina': {'joule': 3.6e+6, 'calorie': 8.6e+5, 'electronvolt': 2.247e+25}
    }
    try:
        return amount * units[from_unit][to_unit]
    except KeyError:
        return "špatná jednotka!"

def main():
    while True:
        print("Vyber kategorii převodu:")
        print("1. Měna")
        print("2. Vzdálenost")
        print("3. Hmotnost")
        print("4. Energie")
        print("5. Konec")
        
        choice = input("Zadej číslo kategorie: ")
        
        if choice == '5':
            print("Konec programu.")
            break
        
        amount = float(input("Zadej hodnotu: "))
        from_unit = input("Zadej jednotku (z): ")
        to_unit = input("Zadej jednotku (na): ")
        
        if choice == '1':
            result = convert_currency(amount, from_unit, to_unit)
        elif choice == '2':
            result = convert_distance(amount, from_unit, to_unit)
        elif choice == '3':
            result = convert_weight(amount, from_unit, to_unit)
        elif choice == '4':
            result = convert_energy(amount, from_unit, to_unit)
        else:
            result = "Neplatná volba"
        
        print(f"Výsledek: {result}")
        print()

if __name__ == "__main__":
    main()
