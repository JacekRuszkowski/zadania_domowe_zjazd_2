# `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`


def wieksze(liczby: list, x: int) -> print:
    """
    Wypisuje z listy liczby weksze od argumentu x
    :param liczby: lista liczb całkowitych
    :param x: liczba całkowita
    :return: wypisuje nową listę z liczbami większymi od x
    """
    lista_wynik = []
    for i in liczby:
        if i > x:
            lista_wynik.append(i)
    print(lista_wynik)


def czy_dziala():
    assert wieksze([10, 20, 30, 40, 50, 60], 21) == [30, 40, 50, 60]
    assert wieksze([13, 2, 89, 65, 12, 111, 7], 80) == [89, 111]
