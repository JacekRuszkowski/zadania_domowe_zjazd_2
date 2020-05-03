# pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.

def pole_trjkata(a: int, b: int, c: int) -> float:
    """
    Funkcja do liczenie pola trójkąta z wzoru Herona.
    :param a:
    :param b:
    :param c:
    :return:
    """
    import math
    if a + b > c and b + c > a and c + a > b:
        p = (a + b + c) / 2
        wynik = math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        raise ValueError("Z podanych boków nie da się stworzyc trójkąta.")

    return wynik


# wypisanie wyniku:
# print(pole_trjkata(15, 11, 13))

def test_czy_dziala():
    assert pole_trjkata(3, 5, 4) == 6.0

def test_wiele_wartosci():
    wartosci = [(3, 5, 4, 6.0), (5, 7, 6, 14.696938456699069), (9, 11, 13, 48.80765821057183)]
    for a, b, c, wynik in wartosci:
        assert pole_trjkata(a, b, c) == wynik
