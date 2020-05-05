# srednia(liczby)` - zwraca średnią wartość z listy `liczby`

from typing import List

def srednia(lista: List[int]) -> int:
    """
    Funkcja do liczenia srednie z elementów z listy
    :param lista: lista liczb całokowitych
    :return: wynik - srednia arytmetyczna
    """
    dodawanie = 0
    for i in lista:
        dodawanie += i

    wynik = dodawanie / len(lista)

    return wynik

lista = [56, 8, 30]

print(srednia(lista))


def test_czy_dziala():
    assert srednia([56, 8, 30], ) == 31.333333333333332

def test_jedna_liczba():
    assert srednia([5]) == 5
    


