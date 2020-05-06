# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`


def ile_wiekszych(liczby: list, x: int) -> int:
    """
    Zwraca ile elementów listy `liczby` jest większych od liczby `x`
    :param liczby:
    :param x:
    :return:
    """
    liczby_wieksze = []

    for i in liczby:
        if i > x:
            liczby_wieksze.append(i)

    wynik = len(liczby_wieksze)

    return wynik


def test_czy_dziala():
    assert ile_wiekszych([10, 20, 30, 40, 5, 70, 45], 20) == 4
    assert ile_wiekszych([10, 20, 15], 30) == 0
    assert ile_wiekszych([15, 2, 65, 80, 55, 14, 21, 36], 5) == 7
