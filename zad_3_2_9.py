# - `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`


def wypisz_podzielne(liczby: list, x: int) -> print:
    podzielne = []

    for i in liczby:
        if i % x == 0:
            podzielne.append(i)

    print(podzielne)


def test_czy_dziala():
    assert wypisz_podzielne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == print([2, 4, 6, 8, 10])
    assert wypisz_podzielne([1, 3, 5, 7, 9], 2) == print(None)

