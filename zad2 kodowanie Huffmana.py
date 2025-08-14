def oblicz_czestotliwosc(tekst):
    czestotliwosci={}
    for znak in tekst:
        czestotliwosci[znak]=czestotliwosci.get(znak,0)+1
    return czestotliwosci
class Wezel:
    def __init__(self,znak,czestotliwosc):
        self.znak=znak
        self.czestotliwosc=czestotliwosc
        self.lewo=None
        self.prawo=None
def zbuduj_drzewo(czestotliwosci):
    wezly=[Wezel(znak,czestotliwosc) for znak,czestotliwosc in czestotliwosci.items()]
    while len(wezly)>1:
        wezly.sort(key=lambda x: x.czestotliwosc)
        lewy=wezly.pop(0)
        prawy=wezly.pop(0)
        nowy_wezel=Wezel(None, lewy.czestotliwosc + prawy.czestotliwosc)
        nowy_wezel.lewo=lewy
        nowy_wezel.prawo=prawy
        wezly.append(nowy_wezel)
    return wezly[0]
def generuj_kod(wezel, kod="", mapa_kodow=None):
    if mapa_kodow is None:
        mapa_kodow={}
    if wezel.znak is not None:
        mapa_kodow[wezel.znak]=kod
        return mapa_kodow
    if wezel.lewo:
        generuj_kod(wezel.lewo, kod + "1", mapa_kodow)
    if wezel.prawo:
        generuj_kod(wezel.prawo, kod + "0", mapa_kodow)
    return mapa_kodow
def zakoduj_tekst(tekst,mapa_kodow):
    return "".join(mapa_kodow[znak] for znak in tekst)
def dekoduj_tekst(kod_binarny,drzewo):
    odwrocone_kody = {kod: znak for znak, kod in drzewo.items()}
    tekst = ""
    obecny_kod = ""
    for bit in kod_binarny:
        obecny_kod += bit
        if obecny_kod in odwrocone_kody:
            tekst += odwrocone_kody[obecny_kod]
            obecny_kod = ""
    return tekst

def kodowanie_Huffmana(tekst):
    czestotliwosci=oblicz_czestotliwosc(tekst)
    drzewo=zbuduj_drzewo(czestotliwosci)
    mapa_kodow=generuj_kod(drzewo)
    kod_binarny=zakoduj_tekst(tekst,mapa_kodow)
    print("Czestotliwosci znakow: ", czestotliwosci)
    print("Mapa kodow: ", mapa_kodow)
    print(f"Zakodowany tekst '{tekst}' to: {kod_binarny}")
    #return kod_binarny,drzewo
def dekodowanie_Huffmana(kod_binarny,drzewo):
    tekst=dekoduj_tekst(kod_binarny,drzewo)
    print(f"Ciag: {kod_binarny} zostal zdekodowany jako: '{tekst}'")
    #return tekst

tekst1=input("Podaj tekst do zakodowania: ")
kodowanie_Huffmana(tekst1)
tekst2=input("Podaj tekst do deszyfrowania: ")
kod_2={}
liczba_par=int(input("Podaj ile par litera-kod masz: "))
for i in range(liczba_par):
    max_proby=3
    for proba in range(1,max_proby+1):
        try:
            dane=input("Wpisz JEDNA litere i jej kod oddzielone przecinkiem. (np. a,011).): ")
            if "," not in dane:
                raise ValueError("Blednie wprowadzona para, brak przecinka")
            litera, kod = dane.split(",",1)
            kod_2[litera] = kod
            print(f"Dodano pare: {litera} -> {kod}")
            break
        except ValueError as e:
            print(f"Blad: {e}")
            if proba == max_proby:
                print("Przekroczono maksymalna liczbe prob. Pomijam te pare.")
            else:
                print("Sprobuj ponownie wprowadzic te pare.")
    print("Ostateczny slownik do dekodowania: ", kod_2)
dekodowanie_Huffmana(tekst2,kod_2)
