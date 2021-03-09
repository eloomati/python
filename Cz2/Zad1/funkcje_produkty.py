from .produkty import magazyn, aktualizacja_ilosc


zamowienie = [
    {
        "produkt":"chleb",
        "ilosc": 10,
        "cena_zamowienia": 23
    }
]

def skladanie_zamowienia(nazwa_produktu, ilosc):
    cena=magazyn[nazwa_produktu]["cena"]
    dostepne_produkty=magazyn[nazwa_produktu]["ilosc"]

    if dostepne_produkty<ilosc:
        print("Brak na magazynie")
        return None

    ostateczna_cena=cena*ilosc
    nowe_zamowienie={
        "produkt":nazwa_produktu,
        "ilosc":ilosc,
        "cena_zamowienia":ostateczna_cena
    }

    aktualizacja_ilosc(nazwa_produktu, ilosc)
    zamowienie.append(nowe_zamowienie)
    return nowe_zamowienie

