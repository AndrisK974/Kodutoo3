def lineaarotsing(massiiv, l, otsitav):						# Defineerin lineaarotsingu. Sisaldab see massiivi, len(), mis tagastab massiivis olevate elementide arvu
    for i in range(l):										# ning otsitavat väärtust. 
        if(massiiv[i] == otsitav):							# Kui massiivis leidub otsitav, tagastatakse otsitav väärtus
            return i
    return -1												# Vastasel juhul tagastatakse -1

massiiv = [1, 26, 19, 23, 288, 5, 12, 3]					# Ette antud massiiv
otsitav = 3													# Otsitav väärtus
l = len(massiiv)											# l on massiivis oleva elemendi arvuline väärtus
indeks = lineaarotsing(massiiv, l, otsitav)					# Defineerin indeksi, et saaksin kontrollida, kas arv esineb massiivis või mitte
if(indeks == -1):											# Kui indeks on -1 (return -1), siis järelikult arvu ei ole massiivis
    print("Otsitud arvu väärtus on: ", otsitav)
    print("Otsin väärtust massiivist: ", massiiv)
    print("Otsitavat väärtust ei esine antud massivis")
else:														# Vastasel juhul arv esineb massiivis ning prinditakse otsitav arv, massiiv, kust seda otsitakse
    print("Otsitud arvu väärtus on: ", otsitav)				# Ning selle arvu indeks
    print("Otsin väärtust massiivist: ", massiiv)
    print("Arv leitud indeksilt: ", indeks)
# Antud algoritmi keerukus on parimal juhul O(1), kuna otsitav element võib olla kõige esimene
# ning halvimal juhul O(n), kuna kõiki elemente võrreldakse järjest ühe korra ning alles lõppu jõudes selgub
# kas element on massiivis või ei ole. O(n) on keerukus ka juhul, kui element on viimane, kuna ikka tuleb kõik elemendid
# ühe kaupa läbi käia.