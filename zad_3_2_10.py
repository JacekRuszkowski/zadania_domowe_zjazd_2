# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma

def pierwsza_podzielna(liczby: list, x: int) -> int:
    """
    Zwraca pieerwszą podzileną przez x z listy 'liczby'
    :param liczby:lista liczb całkowitych
    :param x: dzielnik
    :return: wynik - pierwsza liczba podzilna przez 'x'
    """

    for i in liczby:
        if i % x == 0:
            wynik = i

            return wynik

# print(pierwsza_podzielna([1, 3, 5, 5, 9], 2))

def test_czy_dziala():
    assert pierwsza_podzielna([1, 3, 5, 6, 8, 5, 10], 2) == 6
    assert pierwsza_podzielna([1, 89, 65, 14, 141, 30, 15], 7) == 14
    assert pierwsza_podzielna([1, 3, 5, 5, 9], 2) is None

