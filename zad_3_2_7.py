# suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`


def suma_wiekszych(liczby: list, x: int) -> int:
    """
    Zwraca sumę liczb z listy, które są większe niż `x`
    :param liczby: lista liczb całkowitych
    :param x: liczba całkowita
    :return:
    """
    liczby_wieksze = []
    dodawanie = 0

    for i in liczby:
        if i > x:
            liczby_wieksze.append(i)

    for i in liczby_wieksze:
        dodawanie += i

    return dodawanie


def test_czy_dziala():
    assert suma_wiekszych([10, 20, 30, 40, 5, 70, 45], 20) == 185
    assert suma_wiekszych([10, 20, 15], 30) == 0
