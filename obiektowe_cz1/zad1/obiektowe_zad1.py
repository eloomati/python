class Produkt:
    pass

class Zamowienie:
    pass

class Jablko:
    pass

class Ziemniak:
    pass

if __name__ == '__main__':

    zielone = Jablko()
    czerwone = Jablko()
    slodkie = Jablko()

    smaczne = Ziemniak()
    polskie = Ziemniak()
    maly = Ziemniak()

    print("Typ jabłka to:", type(zielone))
    print("Typ ziemniaka to: ", type(smaczne))

    lista = [Zamowienie(), Zamowienie(), Zamowienie(), Zamowienie(), Zamowienie()]
    print(lista)

    slownik = {
        "Jabłko": Produkt(),
        "Ziemniak": Produkt(),
        "Mleko": Produkt(),
        "Chleb": Produkt
    }
    print(slownik)