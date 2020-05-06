# - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma


def pierwsza_wieksza(lista: list, x: int) -> int:
    """
    Wypisuje pierwszą liczbę z listy, która jest większa od x
    :param lista: Lista liczb całkowitych
    :param x: Liczba całkowita
    :return: Pierwsza liczba większa od x
    """
    for i in lista:
        if i > x:
            return i


def czy_dziala():
    assert pierwsza_wieksza([2, 4, 6, 8, 9], 5) == 6
    assert pierwsza_wieksza([-5, -21, -2, -14, -115], -22) == -21
    assert pierwsza_wieksza([15, 45, 21, 7, 4], 110) is None
