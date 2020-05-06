# - `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona


def maksymalna(lista: list) -> int:
    """
    Funkcja licząca największą liczbę z lity
    :param lista: lista liczb całkowitych
    :return: maksymalna liczba z listy
    """
    wynik = None
    for i in lista:
        if wynik is None or i > wynik:
            wynik = i

    return wynik


def test_czy_dziala():
    assert maksymalna([10, 20, 30, 40, 50]) == 50
    assert maksymalna([1, 8, 4, 9, 2]) == 9
    assert maksymalna([21, 659, 55, 41, 65]) == 659
    assert maksymalna([29, 5, 1, 65, 112]) == 112
