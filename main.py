
STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'no']

def ucitaj_tekst(filepath):

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena.")
        return None


def ocisti_tekst(tekst):
    
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '„', '“', '-', '–']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci


def broji_rijeci(lista_rijeci):
    brojac_rijeci = {}
    for rijec in lista_rijeci:
        brojac_rijeci[rijec] = brojac_rijeci.get(rijec, 0) + 1
    return brojac_rijeci


def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, freq in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = freq
    return ocisceni_rjecnik


def sortiraj_i_ispisi(rjecnik_frekvencija):
    sortirana_lista = sorted(rjecnik_frekvencija.items(), key=lambda item: item[1], reverse=True)
    print("\n--- Top 15 najčešćih riječi ---")
    for i, (rijec, freq) in enumerate(sortirana_lista[:15], start=1):
        print(f"{i}. {rijec}: {freq}")
    print("-" * 30)


if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        lista_rijeci = ocisti_tekst(ucitani_tekst)
        brojac_rijeci = broji_rijeci(lista_rijeci)
        ocisceni_rjecnik = ukloni_stop_words(brojac_rijeci, STOP_WORDS)
        sortiraj_i_ispisi(ocisceni_rjecnik)
    else:
        print("Greška: nije moguće učitati datoteku.")
    
    
    
    


