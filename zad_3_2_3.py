# - `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona



from typing import List

def maksymalna(lista: List[int]) -> int:
    """
    Funkcja licząca największą liczbę z lity
    :param lista: lista liczb całkowitych
    :return: maksymalna liczba z listy
    """
    wynik = 0
    for i in lista:    # TODO zmienic na None
        if i >= wynik:
            wynik = i

    return wynik

lista = [10, 20, 30, 40, 50]

# print(maksymalna(lista))

def test_czy_dziala():
    assert maksymalna([10, 20, 30, 40, 50]) == 50
    assert maksymalna([1, 8, 4, 9, 2]) == 9
    assert maksymalna([21, 659, 55, 41, 65]) == 659
    assert maksymalna([29, 5, 1, 65, 112]) == 112
