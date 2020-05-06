# bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

def bmi(waga: float, wzrost: float) -> float:
    """
    Program do obliczania BMI z podanych przez uzytkownika danych.
    :param waga: waga podana przez użytkownika
    :param wzrost: wzrost podany przez użytkownika
    :return:
    """
    wynik = waga / wzrost ** 2

    return wynik


waga = float(input('Podaj swoją wagę w kilogramach: '))
wzrost = float(input('Podaj swój wzrost w metrach: '))


if bmi(waga, wzrost) < 18.5:
    print(f"BMI wynosi {bmi(waga, wzrost):.2f}. Masz niedowagę.")
elif 18.5 <= bmi(waga, wzrost) <= 24.9:
    print(f"BMI wynosi {bmi(waga, wzrost):.2f}. Twoja waga jest prawidłowa.")
elif 25 <= bmi(waga, wzrost) <= 29.9:
    print(f"TBMI wynosi {bmi(waga, wzrost):.2f}. Masz nadwagę.")
elif bmi(waga, wzrost) > 30:
    print(f"BMI wynosi {bmi(waga, wzrost):.2f}. Cierpisz na otyłość.")


# def test_czy_dziala():
#     assert bmi(87, 1.84) == 25.697069943289225
