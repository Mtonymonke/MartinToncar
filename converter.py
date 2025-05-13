class Converter:
    @staticmethod
    # funkce do které předáváme hodnoty z converter_app
    def convert(value: float, from_unit: str, to_unit: str):
        # řešení převodů pomocí funkce case
        vysledek1=None
        match from_unit:
            case "Kč":
                match to_unit:
                    case "Kč":
                        vysledek1 = value
                    case "Euro":
                        vysledek1 = value/25
                    case "Dolar":
                        vysledek1 = value/24
            case "Euro":
                match to_unit:
                    case "Kč":
                        vysledek1 = value*25
                    case "Euro":
                        vysledek1 = value
                    case "Dolar":
                        vysledek1 = value*1.126
            case "Dolar":
                match to_unit:
                    case "Kč":
                        vysledek1 = value*24
                    case "Euro":
                        vysledek1 = value*0.888435
                    case "Dolar":
                        vysledek1 = value

            case "loket":
                match to_unit:
                    case "loket":
                        vysledek1 = value
                    case "sah":
                        vysledek1 = value/3
                    case "pid":
                        vysledek1 = value*3
                    case "palec":
                        vysledek1 = value/24
                    case "stopa":
                        vysledek1 = value*2
            case "sah":
                match to_unit:
                    case "loket":
                        vysledek1 = value*3
                    case "sah":
                        vysledek1 = value
                    case "pid":
                        vysledek1 = value
                    case "palec":
                        vysledek1 = value/24
                    case "stopa":
                        vysledek1 = value*74.65
            case "pid":
                match to_unit:
                    case "loket":
                        vysledek1 = value*2.8
                    case "sah":
                        vysledek1 = value/9
                    case "pid":
                        vysledek1 = value
                    case "palec":
                        vysledek1 = value*8.3
                    case "stopa":
                        vysledek1 = value*0.69
            case "palec":
                match to_unit:
                    case "loket":
                        vysledek1 = value/20
                    case "sah":
                        vysledek1 = value/75
                    case "pid":
                        vysledek1 = value*1.126
                    case "palec":
                        vysledek1 = value/24
                    case "stopa":
                        vysledek1 = value/24
            case "stopa":
                match to_unit:
                    case "loket":
                        vysledek1 = value*25
                    case "sah":
                        vysledek1 = value
                    case "pid":
                        vysledek1 = value*1.126
                    case "palec":
                        vysledek1 = value/24
                    case "stopa":
                        vysledek1 = value/24

            case "libra":
                match to_unit:
                    case "libra":
                        vysledek1 = value
                    case "unce":
                        vysledek1 = value/25
                    case "kamen":
                        vysledek1 = value/24
                    case "gram":
                        vysledek1 = value/25
                    case "kilogram":
                        vysledek1 = value/24
            case "unce":
                match to_unit:
                    case "libra":
                        vysledek1 = value
                    case "unce":
                        vysledek1 = value/25
                    case "kamen":
                        vysledek1 = value/24
                    case "gram":
                        vysledek1 = value/25
                    case "kilogram":
                        vysledek1 = value/24
            case "kamen":
                match to_unit:
                    case "libra":
                        vysledek1 = value
                    case "unce":
                        vysledek1 = value/25
                    case "kamen":
                        vysledek1 = value/24
                    case "gram":
                        vysledek1 = value/25
                    case "kilogram":
                        vysledek1 = value/24
            case "gram":
                match to_unit:
                    case "libra":
                        vysledek1 = value
                    case "unce":
                        vysledek1 = value/25
                    case "kamen":
                        vysledek1 = value/24
                    case "gram":
                        vysledek1 = value/25
                    case "kilogram":
                        vysledek1 = value/24
            case "kilogram":
                match to_unit:
                    case "libra":
                        vysledek1 = value
                    case "unce":
                        vysledek1 = value/25
                    case "kamen":
                        vysledek1 = value/24
                    case "gram":
                        vysledek1 = value/25
                    case "kilogram":
                        vysledek1 = value/24

            case "joule":
                match to_unit:
                    case "joule":
                        vysledek1 = value
                    case "kalorie":
                        vysledek1 = value/25
                    case "elektronvolt":
                        vysledek1 = value/24
                    case "kilowatthodina":
                        vysledek1 = value/24
            case "kalorie":
                match to_unit:
                    case "joule":
                        vysledek1 = value
                    case "kalorie":
                        vysledek1 = value/25
                    case "elektronvolt":
                        vysledek1 = value/24
                    case "kilowatthodina":
                        vysledek1 = value/24
            case "elektronvolt":
                match to_unit:
                    case "joule":
                        vysledek1 = value
                    case "kalorie":
                        vysledek1 = value/25
                    case "elektronvolt":
                        vysledek1 = value/24
                    case "kilowatthodina":
                        vysledek1 = value/24
            case "kilowatthodina":
                match to_unit:
                    case "joule":
                        vysledek1 = value
                    case "kalorie":
                        vysledek1 = value/25
                    case "elektronvolt":
                        vysledek1 = value/24
                    case "kilowatthodina":
                        vysledek1 = value/24

        if(vysledek1!=None):
            vysledek = vysledek1
            return round(vysledek, 4)
        else:
            return vysledek1
