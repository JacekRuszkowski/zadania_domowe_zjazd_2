# `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta

from typing import List


def roznica(lista: List[int]) -> int:
    """
    Funkcja wylicza różnicę między maksymalną a minimalną liczba w liście
    :param lista: Lista liczba całkowitych
    :return: wynik - róznica
    """
    najmniejsza = None
    najwieksza = None

    if len(lista) == 0:
        najmniejsza = 0
        najwieksza = 0

    for i in lista:
        if najmniejsza is None or i < najmniejsza:
            najmniejsza = i
        elif najwieksza is None or i > najwieksza:
            najwieksza = i

    wynik = najwieksza - najmniejsza

    return wynik


lista = [1, 2, 3, 4, 5, 6]


# print(roznica(lista))

def test_czy_dziala():
    assert roznica([1, 2, 3, 4, 5, 6]) == 5
    assert roznica([]) == 0
    assert roznica ([-15, 12, 10, 15]) == 30
    assert roznica([15, 65, 23, 87, 2]) == 85
