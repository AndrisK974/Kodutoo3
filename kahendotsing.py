def kahendotsing(massiiv, esimene, viimane, otsitav):	# Defineerin massiivi, esimese elemendi, viimase elemendi ja otsitava väärtuse
    
    if viimane >= esimene:								# Vaatan, kas massiiv on sorditud
        keskmine = (viimane + esimene) // 2				# Keskmine indeks on esimene plus viimane jagatud kahega
    
        if massiiv[keskmine] == otsitav:				# Kui keskmine väärtus ongi see mida otsime, tagastame selle väärtuse
            return keskmine
    
        elif massiiv[keskmine] > otsitav:				# Kui otsitav väärtus on väiksem kui keskmine, siis on väärtus keksmisest vasakul
            return kahendotsing(massiiv, esimene, keskmine - 1, otsitav)
    
        else:											# Kui otsitav pole võrdne ega väiksem kui keskmine, siis see on suurem ning see asub keskmisest paremal
            return kahendotsing(massiiv, keskmine + 1, viimane, otsitav)
    
    else:
        return -1										# Kui otsitavat arvu massiivis pole, tagastame -1
    
 
massiiv = [1, 2, 3, 4, 5, 6, 7, 8, 9]
otsitav = 7

indeks = kahendotsing(massiiv, 0, len(massiiv)-1, otsitav)

if indeks == -1:
    print("Arvu", otsitav, "ei esine massiivis", massiiv)
else:
    print("Arv", otsitav, "leitud indeksilt: ", indeks)