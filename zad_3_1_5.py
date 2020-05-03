# bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

def bmi(waga: float, wzrost: float) -> float:
    """
    Program do obliczania BMI z podanych przez uzytkownika danych.
    :param waga:
    :param wzrost:
    :return:
    """
    wynik = waga / wzrost ** 2

    if wynik < 18.5:
        print("Masz niedowagę.")
    elif 18.5 <= wynik <= 24.9:
        print("Twoja waga jest prawidłowa.")
    elif 25 <= wynik <= 29.9:
        print("Masz nadwagę.")
    elif wynik > 30:
        print("Cierpisz na otyłość.")

    return wynik

# Wproawadzanie danych od uzytkownika:
#
# waga = float(input('Podaj swoją wagę w kilogramach: '))
# wzrost = float(input('Podaj swój wzrost w metrach: '))
#
# print(f"BMI wynosi {bmi(waga, wzrost):.1f}")

def test_czy_dziala():
    assert bmi(87, 1.84) == 25.697069943289225

