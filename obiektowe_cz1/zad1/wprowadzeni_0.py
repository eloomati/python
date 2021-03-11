#ZADANIE Z POROWNYWANIEM
# wartosc_jablka = float(input("Jaka jest cena jabłek?: "))
# wartosc_gruszek = float(input("Jaka jest cena gruszek?: "))
# wartosc_pomidorow = float(input("Jaka jest cena pomidorów?: "))

#print(f"Jadłka są droższe od gruszek?: {wartosc_jablka>wartosc_gruszek}. Czy jabłka są droższe od pomidorów?: {wartosc_jablka>wartosc_pomidorow}")
#print(f"Gruszki sa droższe od jablek?: {wartosc_gruszek>wartosc_jablka}. Czy gruszki są droższe od pomidorów?: {wartosc_gruszek>wartosc_pomidorow}")
#print(f"Pomidory są droższe od jabłek?: {wartosc_pomidorow>wartosc_jablka}. CZy pomidory są droższe od gruszek?: {wartosc_pomidorow>wartosc_jablka}")

#PRZERABIANIE Z IF/ELSE
# if wartosc_jablka>wartosc_gruszek:
#     print("Jabka sa drozsze od gruszek")
# else:
#     print("Jablka sa tansze od gruszek")
#
# if wartosc_gruszek>wartosc_pomidorow:
#     print("Gruszki sa drosze od pomidorow")
# else:
#     print("Pomidory są droższe od gruszek")

#ZADANIE Z LISTA
# zakupy = input("Podaj liste zakupów, każdy produkt oddziel przecinkiem: ")
# lista = zakupy.split(", ")
#
# #print(len(lista))
# #print(f"Czy to długa lista? {len(zakupy)>2}.")
#
# #PRZEROBIONE ZADANIE Z LISTA NA IF
# dlugosc_listy=len(lista)
# if dlugosc_listy>3:
#     print("To długa lista!")
# else:
#     print("Krotka lista")

#ZADANIE Z IS i IN
# if ("bułki" or "chleb") in zakupy:
#     print("Na liście są bułki albo chleb")
# else:
#     print("Na liście nie ma ani bułek ani chleba")
# #ZADANIE Z IF NR3
# ocena_matematyka=int(input("Matematyka: "))
# ocena_fizyka=int(input("Fizyka:  "))
# ocena_polski=int(input("Polski: "))
#
# srednia_ocen = float((ocena_matematyka+ocena_fizyka+ocena_polski)/3)
#
# if srednia_ocen>3.5:
#     if ocena_matematyka>1:
#         if ocena_fizyka>1:
#             if ocena_polski>1:
#                 print("Zdałeś")
#             else:
#                 print("Nie zdałeś")
#         else:
#             print("Nie zdałeś")
#     else:
#         print("Nie zdałeś")
# else:
#     print("Nie zdałeś przez średnią")

#SPRAWDZANIE POPRAWNOSCI IMIENIA ZAD3
# imie_uzytkownika = input("Podaj swoje imie: ")
#
# print(imie_uzytkownika[-1])
#
# if imie_uzytkownika[-1] == "a":
#     print("Jesteś kobietą!")
# else:
#     print("Jesteś mężczyzną...")

#UPROSZCZONY KALKULATOR KREDYTOWY

#
# kwota_kredytu = float(input("Podaj kwotę interesującego Cię kredytu: "))
# oprocentowanie_kredytu = int(input("Podaj oprocentowanie kredytu: "))
# wklad_wlasny = float(input("Podaj kwotę wkładu własnego: "))
# czas_w_latach = int(input("Podaj okres czasu kredytu w latach: "))
# przychod_miesieczny = float(input("Podaj swój przychód miesięczny: "))
# suma_miesiecznych_wydatków = float(input("Podaj sumę miesięcznych wydatków: "))
#
# rata_kredytu = (kwota_kredytu*oprocentowanie_kredytu/100)/12+kwota_kredytu/(czas_w_latach*12)
# dostepne_srodki = przychod_miesieczny - suma_miesiecznych_wydatków
# wartosc_nieruchomosci = wklad_wlasny + kwota_kredytu
#
# print(f"Rata kredytu wyjdzie: {rata_kredytu:.2f}")
# print(f"Twoje dostępne środki: {dostepne_srodki:.2f}")
# print(f"Nieruchomość jest warta: {wartosc_nieruchomosci:.2f}")
#
# if ((wklad_wlasny > (20*wartosc_nieruchomosci)/100 and (dostepne_srodki-rata_kredytu) > 1000) or 10*dostepne_srodki/100 < wklad_wlasny > 20*dostepne_srodki/100) and wklad_wlasny > (10*wartosc_nieruchomosci)/100:
#     print("Możesz wziąć kredyt")
# else:
#     print("Nie możesz wziąc kredytu")

#ELIF TEST COOPERA
#
# wiek_uzytkownika = int(input("Podaj swoj wiek: "))
# plec_uzytkownika = input("Podaj swoja plec (K/M): ")
# uzyskany_wynik = float(input("Podaj swoj wynik: "))
#
# if plec_uzytkownika == "K" and 8 <= wiek_uzytkownika <= 12:
#     if 2000 <= uzyskany_wynik <= 1600:
#         print("Dobrze")
#     elif 1600 < uzyskany_wynik <= 1000:
#         print("Srednio")
#     else:
#         print("Słabo")
# elif plec_uzytkownika == "K" and 12 < wiek_uzytkownika <= 20:
#     if 2000 <= uzyskany_wynik <= 1900:
#         print("Dobrze")
#     elif 1900 < uzyskany_wynik <= 1600:
#         print("Srednio")
#     else:
#         print("Słabo")
#
# elif plec_uzytkownika == "K" and 20 < wiek_uzytkownika <= 50:
#     if 2700 <= uzyskany_wynik <= 2200:
#         print("Dobrze")
#     elif 2200 < uzyskany_wynik <= 1800:
#         print("Srednio")
#     else:
#         print("Słabo")
#
# elif plec_uzytkownika == "M" and 8 < wiek_uzytkownika <= 12:
#     if 2200 <= uzyskany_wynik <= 1800:
#         print("Dobrze")
#     elif 1800 < uzyskany_wynik <= 1400:
#         print("Srednio")
#     else:
#         print("Słabo")
#
# elif plec_uzytkownika == "M" and 12 < wiek_uzytkownika <= 20:
#     if 2700 <= uzyskany_wynik <= 2400:
#         print("Dobrze")
#     elif 2200 < uzyskany_wynik <= 2100:
#         print("Srednio")
#     else:
#         print("Słabo")
#
# elif plec_uzytkownika == "M" and 20 < wiek_uzytkownika <= 50:
#     if 2800 <= uzyskany_wynik <= 2400:
#         print("Dobrze")
#     elif 2400 < uzyskany_wynik <= 1600:
#         print("Srednio")
#     else:
#         print("Słabo")
#
# else:
#     print("Nie rozpoznano plc ;(")

#ZADANIE IS i IN
# numer_telefonu=input("Podaj numer telefonu: ")
#
# if "0" in numer_telefonu:
#     print("Jest zero w numerze")
# else:
#     print("Nie ma zera w numerze")

# counter = 0
#
# while counter <= 30:
#    print(counter)
#    counter += 1

#PETLA WHILE ZAD1
# liczba=int(input("Podaj liczbe: "))
# licznik_obrotow=1
#
# while liczba % 2 != 0 and licznik_obrotow < 10:
#     liczba=int(input("Podaj inna liczbe: "))
#     licznik_obrotow += 1
#
# if licznik_obrotow == 10:
#     print("Skonczyly sie proby")
# else:
#     print("Brawo, podales dobra liczbe!")

#PETLA WHILE ZAD 2
# numer_telefonu = input("Podaj numer telefonu: ")
# czysc_numer = numer_telefonu.replace("-", "")
# sformatowany_numer = ""
# index_numeru = 0
#
# while index_numeru < len(czysc_numer):
#     if index_numeru %3 == 0 and index_numeru != 0:
#         sformatowany_numer += "-"
#     sformatowany_numer += czysc_numer[index_numeru]
#     index_numeru += 1
#
# print(f"Twoj numer telefonu to: {sformatowany_numer}")

#PETLE WHILE ZAD 3
# dania=input("Powiedz co lubisz: ")
# lista_dan=dania.split(", ")
# index_dania=0
#
# while index_dania < len(lista_dan):
#     print(f"Numer {index_dania} to {lista_dan[index_dania]}")
#     index_dania += 1
