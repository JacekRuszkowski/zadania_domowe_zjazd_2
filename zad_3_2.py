# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
#
# Logikę obliczania liczby dni wydziel do osobnej funkcji.
#
# **Wersja A**
# Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
#
# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.


def ile_dni(miesiac: str) -> str:
    """
    Funkcja do wypisania dni miesiąca.
    :param miesiac: nazwa iesiąca
    :return:
    """
    if miesiac == "styczeń" or "marzec" or "maj" or "lipiec" or "sierpień" or "październik" or "grudzień":
        wynik = 31
    elif miesiac == "kwiecień" or "czerwiec" or "wrzesień" or "listopad":
        wynik = 30

    return wynik


def rok_przestepny(rok: int) -> int:
    """
    Funkcja do liczenia lat przestępnych
    :param rok:
    :return:
    """
    if rok % 4 == 0 and rok % 100 != 0:
        wynik = 29
    else:
        wynik = 28

    return wynik


miesiace = (
    "styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik",
    "listopad", "grudzień")

while True:
    miesiac = input("Podaj nazwę miesiąca, a powiem Ci ile ma dni: ")
    if miesiac.lower() in miesiace and miesiac.lower() != "luty":
        ilosc_dni = ile_dni(miesiac)
        print(f"{miesiac.capitalize()} ma {ilosc_dni} dni.")
        break
    elif miesiac.lower() == "luty":
        rok = int(input("Podaj rok: "))
        ilosc_dni = rok_przestepny(rok)
        print(f"W roku {rok} luty ma {ilosc_dni} dni.")
        break
    else:
        print("Nie ma takiego miesiąca.")
        continue


# TESTY


