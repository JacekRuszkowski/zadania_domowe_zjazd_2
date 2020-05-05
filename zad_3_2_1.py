# `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona

from typing import List

def suma(lista: List[int]) -> int:
    """
    Funkcja do liczenie sumy elementów z listy
    :param lista:
    :return:
    """
    wynik = 0
    for i in lista:
        wynik += i

    return wynik


lista = [1, 7, 3, 17, 8, 24]

# print(suma(lista))


def test_czy_dziala():
    assert suma([1, 7, 3, 17, 8, 24]) == 60
    assert suma([2, 5]) == 7
    assert suma([-3, 3, 8]) == 8
