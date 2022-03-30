import math

with open("persons.txt",encoding="utf-8") as file:
    with open("gecenler.txt","w",encoding="utf-8") as gecenler:
        with open("kalanlar.txt","w",encoding="utf-8") as kalanlar:
            content = file.readlines()
            s  = 0
            liste = ["AD","SOYAD","BÖLÜM","BİRİNCİ VİZE","İKİNCİ VİZE","FİNAL","ORTALAMA","DURUM"]
            for i in range(len(liste)):

                gecenler.write(liste[i])
                gecenler.write(" "*(30-len(liste[i])))
                kalanlar.write(liste[i])
                kalanlar.write(" " * (30 - len(liste[i])))
            gecenler.write("\n")
            kalanlar.write("\n")
            for satir in content:
                if s == 0:
                    s+=1
                    continue
                satir = satir.replace("\n","")
                index = 0
                bosluk_index = []
                for karakter in satir:
                    if karakter == " ":
                        bosluk_index.append(index)
                    index +=1
                ad_soyad = satir[:bosluk_index[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) -1].replace("-"," ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = birinci_vize*0.3+ ikinci_vize*0.3 +final*0.4
                bolum = satir[bosluk_index[0]+1:bosluk_index[-1]]
                if ortalama >=70 and final >=70:
                    gecenler.write(ad)
                    gecenler.write(" "*(30-len(ad)))
                    gecenler.write(soyad)
                    gecenler.write(" " * (30 - len(soyad)))
                    gecenler.write(bolum)
                    gecenler.write(" " * (30- len(bolum)))
                    gecenler.write(str(birinci_vize))
                    gecenler.write(" "*(30-len(str(birinci_vize))))
                    gecenler.write(str(ikinci_vize))
                    gecenler.write(" " * (30 - len(str(ikinci_vize))))
                    gecenler.write(str(final))
                    gecenler.write(" " * (30 - len(str(final))))
                    gecenler.write(str(round(ortalama,1)))
                    gecenler.write(" " * 26)
                    gecenler.write("Geçti")
                    gecenler.write("\n")
                else:
                    kalanlar.write(ad)
                    kalanlar.write(" " * (30 - len(ad)))
                    kalanlar.write(soyad)
                    kalanlar.write(" " * (30 - len(soyad)))
                    kalanlar.write(bolum)
                    kalanlar.write(" " * (30 - len(bolum)))
                    kalanlar.write(str(birinci_vize))
                    kalanlar.write(" " * (30 - len(str(birinci_vize))))
                    kalanlar.write(str(ikinci_vize))
                    kalanlar.write(" " * (30 - len(str(ikinci_vize))))
                    kalanlar.write(str(final))
                    kalanlar.write(" " * (30 - len(str(final))))
                    kalanlar.write(str(round(ortalama, 1)))
                    kalanlar.write(" " * 26)
                    kalanlar.write("Kaldı")
                    kalanlar.write("\n")