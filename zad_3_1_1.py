# stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry

def stopy_na_metry(stopa: float) -> float:
    """
    Program do przeliczania stop na metr.
    :param stopa: Dane w stopach
    :return: Wynik w metrach
    """
    wynik = stopa * 0.3048

    return wynik


print(f"długość w metrach = {stopy_na_metry(113.5):.2f}")


# TESTY

def test_czy_dziala():
    assert stopy_na_metry(50) == 15.24


def test_na_bledna_odpowiedz():
    assert stopy_na_metry(13) == 2
