magazyn ={
    "chleb": {
        "ilosc": 100,
        "cena": 2.3
    },
    "mleko":{
        "ilosc": 40,
        "cena": 4.2,
    },
    "ser":{
        "ilosc":200,
        "cena": 10.5,
    },
    "gruszki":{
        "ilosc": 20,
        "cena": 1.1
    }
}

def aktualizacja_ilosc(nazwa_produktu, ilosc):
    magazyn[nazwa_produktu]["ilosc"] -= ilosc