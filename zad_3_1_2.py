# max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona

def max_z_dwoch_liczb(a: int, b: int) -> int:
    """
    Funkcja wyliczająca maksimum z dwóch liczb całkowitych podaych przez użytkownika
    :param a: pierwsza liczba całkowita
    :param b: druga liczba całkowita
    :return: maksimum z dwóch liczb
    """

    if a > b:
        wynik = a
    elif b > a:
        wynik = b
    else:
        print("Obie liczby są sobie równe.")
        wynik = a

    return wynik


print(f"Maximum z podanych liczb to {max_z_dwoch_liczb(a = int(input('Podaj pierwszą liczbę: ')), b = int(input('Podaj pierwszą liczbę: ')))}")





# TESTY

def test_czy_dziala():
    assert max_z_dwoch_liczb(2, 45) == 45


def test_bledny():
    assert max_z_dwoch_liczb(5, 9) != 5


def test_na_rowne_wartosci():
    a = 5
    b = 5
    if a == b:
        assert max_z_dwoch_liczb(a, b) == b or a


def test_na_ujemne():
    assert max_z_dwoch_liczb(-5, -63) == -5

