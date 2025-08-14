def szyfrowanie_Cezara(tekst,przesuniecie):
    zaszyfrowany_tekst=""
    for znak in tekst:
        if znak.isalpha():
            poczatek=65 if znak.isupper() else 97
            zaszyfrowany_tekst += chr((ord(znak)-poczatek + przesuniecie) % 26 +poczatek)
        else:
            zaszyfrowany_tekst+=znak
    return zaszyfrowany_tekst

def deszyfrowanie_Cezara(tekst,przesuniecie):
    deszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            poczatek = 65 if znak.isupper() else 97
            deszyfrowany_tekst += chr((ord(znak) - poczatek - przesuniecie) % 26 + poczatek)
        else:
            deszyfrowany_tekst += znak
    return deszyfrowany_tekst



dzialanie='a'
while dzialanie:
    dzialanie = input("Wpisz 'sz' jesli chcesz szyfrowac lub 'ds' jesli chcesz deszyfrowac tekst z szyfru Cezara: ")
    if dzialanie=='sz':
        tekst=input("Podaj tekst do zaszyfrowania: ")
        przesuniecie = int(input("Podaj wartosc przesuniecia do szyfru Cezara: "))
        wynik=szyfrowanie_Cezara(tekst,przesuniecie)
        print(f"Tekst: '{tekst}' zaszyfrowany szyfrem Cezara to: '{wynik}'")
        break
    if dzialanie=='ds':
        tekst = input("Podaj tekst do deszyfrowania: ")
        przesuniecie = int(input("Podaj wartosc przesuniecia do szyfru Cezara: "))
        wynik = deszyfrowanie_Cezara(tekst, przesuniecie)
        print(f"Tekst: '{tekst}' deszyfrowany szyfrem Cezara to: '{wynik}'")
        break
    else:
        pass