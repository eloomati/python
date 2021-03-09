from Cz2.Zad1.funkcje_produkty import skladanie_zamowienia

def run_sklep():
    print("witaj w sklepie, prosze zlozyć zamowienie")
    nazwa_produktu = input("Podaj nazwe produktu: ")
    ilosc = int(input("Podaj potrzebna ilosc: "))

    result = skladanie_zamowienia(nazwa_produktu, ilosc)
    if result is not None:
        cena_ostateczna = result["cena_zamowienia"]
        print(f"Laczny koszt wyniesie: {cena_ostateczna} ZL")

if __name__=='__main__':
    run_sklep()