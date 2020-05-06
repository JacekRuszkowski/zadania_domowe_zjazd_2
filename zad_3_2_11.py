# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`,
# jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
import pytest


def znajdz_wspolny(liczby_1: list, liczby_2: list) -> list:
    if not isinstance(liczby_1, list) or not isinstance(liczby_2, list):
        raise TypeError

    wspolne = []
    for i in liczby_1:
        if i in liczby_2:
            wspolne.append(i)

    if len(wspolne) > 0:
        return wspolne


# RANDOMOWE GENEROWANIE LISTY

# import random
#
# liczby_1 = []
# for i in range(0, 5):
#     n = random.randint(1, 30)
#     liczby_1.append(n)
#
# liczby_2 = []
# for i in range(0, 5):
#     n = random.randint(1, 30)
#     liczby_2.append(n)
#
# # printowanie z funkcji
# print(f"{liczby_1} \n{liczby_2}")
# print(znajdz_wspolny(liczby_1, liczby_2))


# TESTY

def test_czy_dziala():
    assert znajdz_wspolny([28, 10, 13, 28, 4, 26, 9, 23, 5, 30], [26, 27, 8, 12, 4, 22, 1, 18, 28, 26]) == [28, 28, 4,
                                                                                                            26]
    assert znajdz_wspolny([30, 22, 22, 1, 22], [30, 11, 22, 7, 12]) == [30, 22, 22, 22]
    assert znajdz_wspolny([24, 23, 18, 20, 9], [17, 16, 27, 11, 27]) is None


def test_czy_lista():
    with pytest.raises(TypeError):
        znajdz_wspolny((1, 2, 3), (4, 5, 6))
