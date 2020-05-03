# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
print()
print("Kalkulator odległości (mile, kilometry)")
print()


def mile_na_kilometry(odleglosc: float) -> float:
    """
    Przelicza mile na kilometry
    :param odleglosc: odległosc w mila
    :return: wynik - odległosc w kilometrach
    """
    wynik = odleglosc * 1.609344

    return wynik


def kilometry_na_mile(odleglosc: float) -> float:
    """
    Przelicza kilometry na mile.
    :param odleglosc: odleglosc w kilometrach
    :return: odleglosc w milach
    """
    wynik = odleglosc / 1.609344

    return wynik


while True:
    dzialanie_podane = input(
        "Jaki działanie chcesz wykonać? Mile na kilometry - wpisz 1; ilometry na mile - wpisz 2: ")

    if dzialanie_podane.isdecimal():
        dzialanie = int(dzialanie_podane)

        if dzialanie == 1:
            odleglosc = float(input("Podaj odległość w milach: "))
            print(f"{odleglosc} M to {mile_na_kilometry(odleglosc):.1f} km.")  # tym miejscu wykorzystanie funkcji
            break

        elif dzialanie == 2:
            odleglosc = float(input("Podaj odległość w kilometrach: "))
            print(f"{odleglosc} km to {kilometry_na_mile(odleglosc):.1f} M.")  # tym miejscu wykorzystanie funkcji
            break

        else:
            print("Poproszę o wybranie 1 lub 2.")
            continue

    else:
        print("Poproszę o wybranie 1 lub 2.")
        continue
