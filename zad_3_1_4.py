# pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)

def pole_kola(r: float) -> float:
    """
    Funkcja do obliczania pola koła
    :param r: promień koła podany przez użytkownika
    :return: pole koła
    """
    from math import pi
    wynik = pi * r ** 2

    return wynik  # jak mozna zaokrąglić nie formatując na str?


# Wprawdzenie promienia przez użytkownika:
# print(f"Pole koła o zadanym promieniu wynosi {pole_kola(r=float(input('Podaj promień: '))):.2f}")

print(f"Pole koła o zadanym promieniu wynosi {pole_kola(12)}")


def test_czy_dziala():
    assert pole_kola(15) == 706.8583470577034
    assert pole_kola(5) != 15


def test_przyklady():
    przyklady = [(2, 12.566370614359172), (5, 78.53981633974483), (3, 28.274333882308138), (12, 452.3893421169302)]
    for r, wynik in przyklady:
        assert pole_kola(r) == wynik
