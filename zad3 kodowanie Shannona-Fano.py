def oblicz_czestotliwosc(tekst):
    czestotliwosci={}
    for znak in tekst:
        czestotliwosci[znak]=czestotliwosci.get(znak,0)+1
    return dict(sorted(czestotliwosci.items(), key=lambda item:item[1], reverse=True))   #posortowany slownik wedlug nierosniecia czestowliwosci wystepowania

def podziel_na_grupy(znaki, czestotliwosci):
    if len(znaki) == 1:
        return [znaki, []]
    suma_czestotliwosci = sum(czestotliwosci[znak] for znak in znaki)
    polowa=suma_czestotliwosci / 2
    grupa1, grupa2 = [], []
    suma=0
    for znak in znaki:
        if suma+czestotliwosci[znak] <= polowa:
            grupa1.append(znak)
            suma += czestotliwosci[znak]
        else:
            grupa2.append(znak)
    return [grupa1, grupa2]

def generuj_kod(znaki,czestotliwosci,kod=""):
    if len(znaki) == 1:
        return {znaki[0]: kod}
    grupa1, grupa2 = podziel_na_grupy(znaki,czestotliwosci)
    kody={}
    kody.update(generuj_kod(grupa1,czestotliwosci,kod+"1"))
    kody.update(generuj_kod(grupa2,czestotliwosci,kod+"0"))
    return kody

def szyfruj_shannon_fano(tekst):
    czestotliwosci=oblicz_czestotliwosc(tekst)
    znaki=list(czestotliwosci.keys())
    kody=generuj_kod(znaki,czestotliwosci)
    zaszyfrowany="".join(kody[znak] for znak in tekst)
    return zaszyfrowany,kody

def deszyfruj_shannon_fano(zaszyfrowany, kody):
    odwrocone_kody = {kod: znak for znak, kod in kody.items()}
    tekst=""
    obecny_kod=""
    for bit in zaszyfrowany:
        obecny_kod+=bit
        if obecny_kod in odwrocone_kody:
            tekst+=odwrocone_kody[obecny_kod]
            obecny_kod= ""
    return tekst


tekst=input("Podaj tekst do zaszyfrowania: ")
zaszyfrowany, kody = szyfruj_shannon_fano(tekst)
print(f"\nZaszyfrowany tekst: {zaszyfrowany}")
print(f"Kody znakow: {kody}")

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
odszyfrowany=deszyfruj_shannon_fano(tekst2,kod_2)
print(f"\nOdszyfrowano tekst: '{odszyfrowany}'")


