# srednia` - oblicza średnią z dwóch liczb,

def srednia(a: int, b: int) -> float:
    """
    Program do wyliczania sredniej z dwoch liczb
    :param a: pierwsza liczba
    :param b: druga liczba
    :return:
    """

    wynik = (a + b) / 2

    return wynik


while True:

    podane_a = input("Podaj piewrszą liczbę: ")
    podane_b = input("Podaj drugą liczbą: ")

    if not podane_a.isdigit() or not podane_b.isdigit():
        print("Poproszę o podanie tylko liczb całkowitych.")
        continue

    a = int(podane_a)
    b = int(podane_b)
    break

print(f"Średnia z podanych liczb wynosi {srednia(a, b)}")


# TESTY

# def test_czy_dziala():
#     assert srednia(20, 50) == 35



